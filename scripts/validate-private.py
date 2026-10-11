"""Private consistency checks; never print personal content."""
import hashlib
import json
from pathlib import Path
import subprocess
m=json.loads(Path('build.json').read_text())
for ext,key in [('tex','sourceSha256'),('pdf','pdfSha256')]:
    assert hashlib.sha256(Path('Apoorv_Darshan_Resume.'+ext).read_bytes()).hexdigest()==m[key], 'Build manifest mismatch'
for path in Path('.').glob('*.json'):
    json.loads(path.read_text())
for name in subprocess.check_output(['git','ls-files'],text=True).splitlines():
    p=Path(name)
    if p.suffix not in ['.md','.tex','.json','.yml','.py']: continue
    text=p.read_text()
    assert ('-----BEGIN '+ 'PRIVATE KEY-----') not in text, 'Committed private key'
    assert ('-----BEGIN '+ 'RSA PRIVATE KEY-----') not in text, 'Committed private key'
print('Private manifests and snapshots validated; no content disclosed.')
