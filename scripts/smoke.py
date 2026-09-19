import json,secrets,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();v=lambda n:next(x.split('=',1)[1].strip().strip('"').strip("'") for x in E.splitlines() if x.startswith(n+'='));owner=create_account(account_private_key=v('ACCOUNT_6_GENLAYER_PRIVATE_KEY'));stewards=[create_account(account_private_key='0x'+secrets.token_hex(32)) for _ in range(3)];clients=[create_client(chain=studionet,account=x) for x in [owner]+stewards];addr='0x53f1Ec3e8ea5F7C8c4BA9729D4b2e380755a9567';rid='LIVE-'+str(int(time.time()));commit='0794143';urls=[f'https://raw.githubusercontent.com/wakbowaa/habitat-corridor/{commit}/evidence/parcel-a.txt',f'https://cdn.jsdelivr.net/gh/wakbowaa/habitat-corridor@{commit}/evidence/parcel-b.txt',f'https://github.com/wakbowaa/habitat-corridor/raw/{commit}/evidence/parcel-c.txt'];tx=[]
def send(client,fn,args):
 h=client.write_contract(address=addr,function_name=fn,args=args);r=client.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
send(clients[0],'propose',[rid,'River otter',[x.address for x in stewards],urls]);
for i in range(3):send(clients[i+1],'accept_parcel',[rid,i])
send(clients[0],'observe',[rid,1]);print(json.dumps({'id':rid,'state':'ACTIVE','transactions':tx}),flush=True)
