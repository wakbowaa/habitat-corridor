from conftest import CONTRACT
def test_three_stewards_activate(direct_vm,direct_deploy,direct_accounts):
 direct_vm.sender=direct_accounts[0];x=direct_deploy(CONTRACT);urls=['https://a.example/p','https://b.example/p','https://c.example/p'];x.propose('c-1','River otter',['0x'+a.hex() for a in direct_accounts[1:4]],urls)
 for i in range(3):direct_vm.sender=direct_accounts[i+1];x.accept_parcel('c-1',i);direct_vm.mock_web(r'[abc]\.example',{'status':200,'body':'Adjacent riparian parcel with compatible otter habitat.'})
 direct_vm.mock_llm(r'.*HabitatCorridor spatial check.*','{"connected":true,"gap_indexes":[]}');x.observe('c-1',1);assert x.get_corridor('c-1')['state']=='ACTIVE'
def test_wrong_steward_rejected(direct_vm,direct_deploy,direct_accounts):
 direct_vm.sender=direct_accounts[0];x=direct_deploy(CONTRACT);x.propose('c-1','River otter',['0x'+a.hex() for a in direct_accounts[1:4]],['https://a.example/p','https://b.example/p','https://c.example/p'])
 with direct_vm.expect_revert('assigned unaccepted'):x.accept_parcel('c-1',0)
