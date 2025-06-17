import random
import os
facts = [
    '1. Disable unused services to reduce your attack surface.',
    '2. Use strong, unique passwords and enable 2FA where possible.',
    '3. Keep your system and all packages up-to-date with security patches.',
    '4. Regularly review user accounts and remove unneeded ones.',
    '5. Use the principle of least privilege: only give users the access they need.'
]
fact = random.choice(facts)
os.system(f'echo \"[Cybersecurity Tip] {fact}\" | wall')