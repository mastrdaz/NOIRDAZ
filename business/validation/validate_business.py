#!/usr/bin/env python3
"""Read-only validation of the Noirdaz blank-template release. Standard library only."""
from pathlib import Path
from decimal import Decimal, ROUND_CEILING
import csv, hashlib, json, re, sys, zipfile, xml.etree.ElementTree as ET
B=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
# Relative links and placeholder catalog.
fields={r['field']for r in json.loads((B/'validation/field_catalog.json').read_text())}
md=list(B.rglob('*.md'))
for p in md:
 text=p.read_text()
 for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',dest)or dest.startswith('#'):continue
  target=dest.split('#')[0]
  check((p.parent/target).exists(),f'Broken link {p.relative_to(B)} -> {dest}')
 if p.name not in ['PLACEHOLDER_REFERENCE.md']:
  for token in re.findall(r'\[\[([A-Z0-9_]+)\]\]',text):check(token in fields,f'Unregistered {token} in {p}')
 for token in re.findall(r'\[\[(.*?)\]\]',text):check(bool(re.fullmatch('[A-Z0-9_]+',token)),f'Malformed token {token}')
# Legal suite completeness and status.
legal=list((B/'legal/templates').glob('*.md'))
check(len(legal)==12,f'Expected 12 legal templates, got {len(legal)}')
reference=(B/'legal/PLACEHOLDER_REFERENCE.md').read_text()
for p in legal:
 text=p.read_text();check('ATTORNEY REVIEW' in text,f'Missing review status {p.name}')
 for token in set(re.findall(r'\[\[([A-Z0-9_]+)\]\]',text)):check(token in reference,f'Legal token absent from reference: {token}')
 if p.name!='PRIVACY_DATA_QUESTIONNAIRE.md':
  for token in ['PROVIDER_SIGNATURE','CLIENT_SIGNATURE','PROVIDER_SIGNATORY_NAME','CLIENT_SIGNATORY_NAME']:check('[['+token+']]'in text,f'Missing signature field {p.name}: {token}')
# CSV structure and independent base scenario arithmetic.
rows=list(csv.reader((B/'finance/templates/pricing_calculator.csv').open()))
check(len(rows)==36 and all(len(r)==4 for r in rows),'Pricing CSV shape')
get=lambda col,row:Decimal(rows[row-1][col])
ceil=lambda x:x.quantize(Decimal('.01'),rounding=ROUND_CEILING)
expected=json.loads((B/'validation/pricing_expected.json').read_text())
for col,prefix in [(1,'setup'),(2,'monthly')]:
 cost=get(col,4)*get(col,5)+get(col,7)+(get(col,8)/12 if col==2 else 0)+get(col,10)+get(col,11)
 variable=get(col,13)*(1+get(col,14))+get(col,15);fixed=get(col,17)*get(col,18)
 price=ceil((cost+fixed)/(1-get(col,20)-variable))
 check(price==Decimal(str(expected[prefix+'_recommended'])),f'{prefix} price mismatch')
 margin=(price-cost-fixed-variable*price)/price
 check(margin>=get(col,20),f'{prefix} rounded price below target margin')
for rel in ['finance/templates/cost_ledger.csv','finance/templates/recurring_revenue.csv','vendors/templates/renewals.csv']:
 check(len(list(csv.reader((B/rel).open())))==1,f'Public tracker contains filled rows: {rel}')
# Original repository files remain byte-identical to pinned Git blob hashes.
base=json.loads((B/'validation/preservation_manifest.json').read_text())
for rec in base['files']:
 p=B.parent/rec['path'];check(p.exists(),f'Missing baseline {p}')
 if p.exists():
  content=p.read_bytes();sha=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
  check(sha==rec['sha'],f'Original file changed: {rec["path"]}')
# Optional exported XLSX comparison, no macros/external links or cached formula errors.
if len(sys.argv)>1:
 with zipfile.ZipFile(sys.argv[1])as z:
  check(not any('externalLinks/'in n or n.endswith('vbaProject.bin') or n=='xl/connections.xml'for n in z.namelist()),'Unexpected active/external XLSX component')
  ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
  root=ET.fromstring(z.read('xl/worksheets/sheet1.xml'));forms={c.attrib['r']:c.find('m:f',ns).text for c in root.findall('.//m:c',ns)if c.find('m:f',ns)is not None}
  for i,row in enumerate(rows,1):
   for j,value in enumerate(row):
    if value.startswith('='):check(forms.get(chr(65+j)+str(i))==value[1:],f'CSV/XLSX formula mismatch {i},{j}')
  for n in z.namelist():
   if n.startswith('xl/worksheets/sheet')and n.endswith('.xml'):
    check(not any(c.attrib.get('t')=='e'for c in ET.fromstring(z.read(n)).findall('.//m:c',ns)),f'Cached formula error in {n}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(md)} Markdown files; {len(fields)} registered fields; 12 legal templates; CSV arithmetic/schema; pinned original-file preservation'+('; optional XLSX checks'if len(sys.argv)>1 else ''))
print('Limits: not legal/tax/security certification; no interactive Excel/Sheets or live service test.')
