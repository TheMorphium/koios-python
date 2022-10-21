#!/usr/bin/env python
"""
TESTING SCRIPT FOR KOIOS_PYTHON USING PYTEST

To use this script, you must have pytest installed.
pip install pytest

Change directory to the folder containing this script and run:
pytest

Watch the terminal for the results of the tests. :)

"""

import pytest
import koios_python as kp


# create a new url object with your own url or use koios.rest url by default
kp_mainnet_server = kp.URLs()

kp_custom_server = kp.URLs(url="https://koios-otg.tosidrop.io/")

# Koios server switching to testnet default is mainnet and this feature only works for standard Koios rest api server api.koios.rest/api/v0
kp_testnet_server = kp.URLs( network='testnet')


##############################################################################
# ACCOUNT FUNCTIONS

# get account list
def test_get_account_list():
        account_list_custom = kp_custom_server.get_account_list()
        assert 'code' not in account_list_custom[0]
        
        account_list_mainnet = kp_mainnet_server.get_account_list()
        assert 'code' not in account_list_mainnet[0]
        
        account_list_testnet = kp_testnet_server.get_account_list()
        assert 'code' not in account_list_testnet[0]


# get account info
def test_get_account_info():
        account_info_custom = kp_custom_server.get_account_info("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_info_custom[0]
        
        account_info_mainnet = kp_mainnet_server.get_account_info("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_info_mainnet[0]
        
        account_info_testnet = kp_testnet_server.get_account_info("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_info_testnet[0]

# get account rewards
def test_get_account_rewards():
        account_rewards_custom = kp_custom_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_rewards_custom[0]
        
        account_rewards_mainnet = kp_mainnet_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_rewards_mainnet[0]
        
        account_rewards_testnet = kp_testnet_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_rewards_testnet[0]

        account_rewards_custom = kp_custom_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", 350)
        assert 'code' not in account_rewards_custom[0]
        
        account_rewards_mainnet = kp_mainnet_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", 350)
        assert 'code' not in account_rewards_mainnet[0]
        
        account_rewards_testnet = kp_testnet_server.get_account_rewards("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250", 350)
        assert 'code' not in account_rewards_testnet[0]
        
# get account updates
def test_get_account_updates():
        account_updates_custom = kp_custom_server.get_account_updates("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_updates_custom[0]
        
        account_updates_mainnet = kp_mainnet_server.get_account_updates("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_updates_mainnet[0]
        
        account_updates_testnet = kp_testnet_server.get_account_updates("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        assert 'code' not in account_updates_testnet[0]

# get account assets
def test_get_account_assets():
        account_assets_custom = kp_custom_server.get_account_assets("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_assets_custom) > 0:
                assert 'code' not in account_assets_custom[0]
        
        account_assets_mainnet = kp_mainnet_server.get_account_assets("stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250")
        if len(account_assets_mainnet) > 0:
                assert 'code' not in account_assets_mainnet[0]
        
        account_assets_testnet = kp_testnet_server.get_account_assets(["stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj",
                                                                       "stake_test1uq7g7kqeucnqfweqzgxk3dw34e8zg4swnc7nagysug2mm4cm77jrx"])
        if len(account_assets_testnet) > 0:
                assert 'code' not in account_assets_testnet[0]


        
# get account history
def test_get_account_history():
        account_history_custom = kp_custom_server.get_account_history(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
                                                                       "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"])
        if len(account_history_custom) > 0:
                assert 'code' not in account_history_custom[0]
        
        account_history_mainnet = kp_mainnet_server.get_account_history(["stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250",
                                                                         "stake1uxpdrerp9wrxunfh6ukyv5267j70fzxgw0fr3z8zeac5vyqhf9jhy"])
        if len(account_history_mainnet) > 0:
                assert 'code' not in account_history_mainnet[0]
        
        account_history_testnet = kp_testnet_server.get_account_history(["stake_test1uqrw9tjymlm8wrwq7jk68n6v7fs9qz8z0tkdkve26dylmfc2ux2hj",
                                                                         "stake_test1uq7g7kqeucnqfweqzgxk3dw34e8zg4swnc7nagysug2mm4cm77jrx"])
        if len(account_history_testnet) > 0:
                assert 'code' not in account_history_testnet[0] 
 
##############################################################################
# ADDRESS FUNCTIONS

# get address info
def test_get_address_info():
        address_info_custom = kp_custom_server.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_info_custom) > 0:
                assert 'code' not in address_info_custom[0]
        
        address_info_mainnet = kp_mainnet_server.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_info_mainnet) > 0:
                assert 'code' not in address_info_mainnet[0]
        
        address_info_testnet = kp_testnet_server.get_address_info("addr_test1qzx9hu8j4ah3auytk0mwcupd69hpc52t0cw39a65ndrah86djs784u92a3m5w475w3w35tyd6v3qumkze80j8a6h5tuqq5xe8y")
        if len(address_info_testnet) > 0:
                assert 'code' not in address_info_testnet[0]

# get address transactions
def test_get_address_transactions():
        address_txs_custom = kp_custom_server.get_address_txs(["addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",
                                                                        "addr1qyfldpcvte8nkfpyv0jdc8e026cz5qedx7tajvupdu2724tlj8sypsq6p90hl40ya97xamkm9fwsppus2ru8zf6j8g9sm578cu"])
        if len(address_txs_custom) > 0:
                assert 'code' not in address_txs_custom[0]
         
        address_txs_mainnet = kp_mainnet_server.get_address_txs(["addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",
                                                                          "addr1qyfldpcvte8nkfpyv0jdc8e026cz5qedx7tajvupdu2724tlj8sypsq6p90hl40ya97xamkm9fwsppus2ru8zf6j8g9sm578cu"])
        if len(address_txs_mainnet) > 0:
                assert 'code' not in address_txs_mainnet[0]
        
        address_txs_testnet = kp_testnet_server.get_address_txs(["addr_test1qzx9hu8j4ah3auytk0mwcupd69hpc52t0cw39a65ndrah86djs784u92a3m5w475w3w35tyd6v3qumkze80j8a6h5tuqq5xe8y",
                                                                          "addr_test1qrk7920v35zukhcch4kyydy6rxnhqdcvetkvngeqrvtgavw8tpzdklse3kwer7urhrlfg962m9fc8cznfcdpka5pd07sgf8n0w"])
        if len(address_txs_testnet) > 0:
                assert 'code' not in address_txs_testnet[0]
        
        address_txs_after_block = kp_mainnet_server.get_address_txs("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g",1)
        if len(address_txs_after_block) > 0:
                assert 'code' not in address_txs_after_block[0]

# get address assets 
def test_get_address_assets():
        address_assets_custom = kp_custom_server.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_assets_custom) >0:
                assert 'code' not in address_assets_custom[0]
                
        address_assets_mainnet = kp_mainnet_server.get_address_assets("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g")
        if len(address_assets_mainnet) >0:
                assert 'code' not in address_assets_mainnet[0]
        
        address_assets_testnet = kp_testnet_server.get_address_assets("addr_test1qrk7920v35zukhcch4kyydy6rxnhqdcvetkvngeqrvtgavw8tpzdklse3kwer7urhrlfg962m9fc8cznfcdpka5pd07sgf8n0w")
        if len(address_assets_testnet) >0:
                assert 'code' not in address_assets_testnet[0]

# get payment credentials hash
def test_get_credentials():
        credentials_custom = kp_custom_server.get_credential_txs("025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52")
        if len(credentials_custom) > 0:
                assert 'code' not in credentials_custom[0]
        
        credentials_mainnet = kp_mainnet_server.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52')
        if len(credentials_mainnet) > 0:
                assert 'code' not in credentials_mainnet[0]
        
        credentials_testnet = kp_testnet_server.get_credential_txs('00003fac863dc2267d0cd90768c4af653572d719a79ca3b01957fa79')
        if len(credentials_testnet) > 0:
                assert 'code' not in credentials_testnet[0]
        
        credentials_after_block = kp_mainnet_server.get_credential_txs('025b0a8f85cb8a46e1dda3fae5d22f07e2d56abb4019a2129c5d6c52',6238675)
        if len(credentials_after_block) > 0:
                assert 'code' not in credentials_after_block[0]

        credentials_after_block_testnet = kp_testnet_server.get_credential_txs('00003fac863dc2267d0cd90768c4af653572d719a79ca3b01957fa79',2342661)
        if len(credentials_after_block_testnet) > 0:
                assert 'code' not in credentials_after_block_testnet[0]
'''
##############################################################################
# ASSET FUNCTIONS

# get asset list of all native tokens
def test_get_asset_list():
	asset_list = koios_python.get_asset_list()
	assert 'code' not in asset_list[0]

# get asset address list
def test_get_asset_address_list():
        asset_address_list = koios_python.get_asset_address_list('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
        assert 'code' not in asset_address_list[0]

# get asset info
def test_get_asset_info():
        asset_info = koios_python.get_asset_info('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
        assert 'code' not in asset_info[0]
        
# get asset history
def test_get_asset_history():
	asset_history = koios_python.get_asset_history('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501','424f4f4b')
	assert 'code' not in asset_history[0]
 
# get asset policy info
def test_get_asset_policy_info():
        asset_policy_info = koios_python.get_asset_policy_info('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501')
        assert 'code' not in asset_policy_info[0]

# get asset summary
def test_get_asset_summary():
        asset_summary = koios_python.get_asset_summary('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', '424f4f4b')
        assert 'code' not in asset_summary[0]

# get asset transaction history
def test_get_asset_txs_history():
	asset_txs_history = koios_python.get_asset_txs('750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501', '424f4f4b')
	assert 'code' not in asset_txs_history[0]
'''

##############################################################################
# BLOCK FUNCTIONS

# get list of blocks
def test_get_blocks():
        
        blocks_custom_server = kp_custom_server.get_blocks()
        assert 'code' not in blocks_custom_server[0]
        
        blocks_mainnet_server = kp_mainnet_server.get_blocks()
        assert 'code' not in blocks_mainnet_server[0]
        
        blocks_testnet_server = kp_testnet_server.get_blocks()
        assert 'code' not in blocks_testnet_server[0]
        
# get block info
def test_get_block_info():
        
        block_info_custom = kp_custom_server.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
    						"60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
    						"c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
        assert 'code' not in block_info_custom[0]

        block_info_mainnet = kp_mainnet_server.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
                                                               "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
                                                               "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
        assert 'code' not in block_info_mainnet[0]
        
        block_info_testnet = kp_testnet_server.get_block_info(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30",
                                                               "60188a8dcb6db0d80628815be2cf626c4d17cb3e826cebfca84adaff93ad492a",
                                                               "c6646214a1f377aa461a0163c213fc6b86a559a2d6ebd647d54c4eb00aaab015"])
        assert 'code' not in block_info_testnet[0]


# get block transactions
def test_get_block_txs():
        
        block_txs_custom = kp_custom_server.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
        assert 'code' not in block_txs_custom[0]
        
        block_txs_mainnet = kp_mainnet_server.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
        assert 'code' not in block_txs_mainnet[0]
        
        block_txs_testnet = kp_testnet_server.get_block_txs(["fb9087c9f1408a7bbd7b022fd294ab565fec8dd3a8ef091567482722a1fa4e30"])
        assert 'code' not in block_txs_testnet[0]


##############################################################################
# EPOCH FUNCTIONS

# get epoch info
def test_get_epoch_info():
        
        epoch_info_custom = kp_custom_server.get_epoch_info()
        assert 'code' not in epoch_info_custom[0]

        epoch_info_mainnet = kp_mainnet_server.get_epoch_info()
        assert 'code' not in epoch_info_mainnet[0]
        
        epoch_info_testnet = kp_testnet_server.get_epoch_info()
        assert 'code' not in epoch_info_testnet[0]
 
# get epoch params
def test_get_epoch_params():
        
        epoch_params_custom = kp_custom_server.get_epoch_params()
        assert 'code' not in epoch_params_custom[0]
        
        epoch_params_mainnet = kp_mainnet_server.get_epoch_params()
        assert 'code' not in epoch_params_mainnet[0]
        
        epoch_params_testnet = kp_testnet_server.get_epoch_params()
        assert 'code' not in epoch_params_testnet[0]



##############################################################################
# NETWORK FUNCTIONS

# check tip
def test_get_tip():
        
        tip_custom = kp_custom_server.get_tip()
        assert 'code' not in tip_custom[0]
        
        tip_mainnet = kp_mainnet_server.get_tip()
        assert 'code' not in tip_mainnet[0]
        
        tip_testnet = kp_testnet_server.get_tip()
        assert 'code' not in tip_testnet[0]
        
        
# check genesis info
def test_get_genesis():
        
        genesis_custom = kp_custom_server.get_genesis()
        assert 'code' not in genesis_custom[0]
        
        genesis_mainnet = kp_mainnet_server.get_genesis()
        assert 'code' not in genesis_mainnet[0]
        
        genesis_testnet = kp_testnet_server.get_genesis()
        assert 'code' not in genesis_testnet[0]
        
def test_get_totals():
        
        epoch_totals_custom = kp_custom_server.get_totals()
        assert 'code' not in epoch_totals_custom[0]
        
        epoch_totals_mainnet = kp_mainnet_server.get_totals()
        assert 'code' not in epoch_totals_mainnet[0]
        
        epoch_totals_testnet = kp_testnet_server.get_totals()
        assert 'code' not in epoch_totals_testnet[0]

'''
##############################################################################
# POOL FUNCTIONS

# get list of pools on the network
def test_get_pool_list():
	pool_list = koios_python.get_pool_list('0-10')
	assert 'code' not in pool_list[0]
 
# get pool info
def test_get_pool_info():
        pool_info = koios_python.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp",
    						"pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m",
    						"pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"])
        assert 'code' not in pool_info[0]
        
        
# get pool stake snapshot
def test_get_pool_stake_snapshot():
        stake_snapshot = koios_python.get_pool_stake_snapshot("pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp")
        assert 'code' not in stake_snapshot[0]    

        
# get pool delegator information
def test_get_pool_delegators():
        delegator_info = koios_python.get_pool_delegators("pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp")
        assert 'code' not in delegator_info[0]
        
# get pool delegator history
def test_get_pool_delegators_history():
        
	delegator_history = koios_python.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
	assert 'code' not in delegator_history[0]

	delegator_history_epoch = koios_python.get_pool_delegators_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 320)
	assert 'code' not in delegator_history_epoch[0]

# get pool blocks
def test_get_pool_blocks():
	pool_blocks = koios_python.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
	assert 'code' not in pool_blocks[0]

	pool_blocks_epoch = koios_python.get_pool_blocks("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 320)
	assert 'code' not in pool_blocks_epoch[0]

        
# get pool history
def test_get_pool_history():
	pool_history = koios_python.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc")
	assert 'code' not in pool_history[0]

	pool_history_epoch = koios_python.get_pool_history("pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", 320)
	assert 'code' not in pool_history_epoch[0]

# get pool updates
def test_get_pool_updates():
	pool_updates = koios_python.get_pool_updates()
	assert 'code' not in pool_updates[0]

# get pool relays
def test_get_pool_relays():
	pool_relays = koios_python.get_pool_relays('0-10')
	assert 'code' not in pool_relays[0]
 
# get pool metadata
def test_get_pool_metadata():
	pool_metadata = koios_python.get_pool_metadata()
	assert 'code' not in pool_metadata[0]
 
	pool_metadata_id = koios_python.get_pool_metadata(["pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc", "pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m"])
	assert 'code' not in pool_metadata_id[0]

##############################################################################
# SCRIPT FUNCTIONS

# get list of native scripts on the network
def test_get_native_script_list():
	script_list = koios_python.get_native_script_list('0-10')
	assert 'code' not in script_list[0]

# get plutus script list
def test_get_plutus_script_list():
	script_list = koios_python.get_plutus_script_list('0-10')
	assert 'code' not in script_list[0]

# get list of all redeemers for a given script hash
def test_get_script_redeemers():
        script_redeemers = koios_python.get_script_redeemers('d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8')
        assert 'code' not in script_redeemers[0]
        
##############################################################################
# TRANSACTION FUNCTIONS

# get transaction(s) info
def test_tx_info():
        
        tx_info = koios_python.get_tx_info("0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94")
        assert 'code' not in tx_info[0]
        
        txs_info= koios_python.get_tx_info(["0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94",
                                            "f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e"])
        assert 'code' not in txs_info[0]

# get transaction(s) utxos
def test_get_tx_utxos():
        
        tx_utxos = koios_python.get_tx_utxos("0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94")
        assert 'code' not in tx_utxos[0]
        
        txs_utxos = koios_python.get_tx_utxos(["0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94",
                                               "f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e"])
        assert 'code' not in txs_utxos[0]

# get transaction(s) metadata
def test_get_tx_metadata():
        
        tx_metadata = koios_python.get_tx_metadata("0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94")
        assert 'code' not in tx_metadata[0]
        
        txs_metadata = koios_python.get_tx_metadata(["0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94",
                                                     "f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e"])
        assert 'code' not in txs_metadata[0]

# get transaction(s) metadata labels
def test_get_tx_metalabels():
        
        tx_metalables = koios_python.get_tx_metalabels("0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94")
        assert 'code' not in tx_metalables[0]
        
        txs_metalables = koios_python.get_tx_metalabels(["0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94",
                                                        "f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e"])
        
        assert 'code' not in txs_metalables[0]


# NOT FINISHED
# submit_tx signed cbor
# def test_submit_tx():
	
# 	tx_submit = koios_python.submit_tx("file")
# 	assert 'code' not in tx_submit[0]

# get tx status
def test_get_tx_status():
        
        tx_status = koios_python.get_tx_status("0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94")
        assert 'code' not in tx_status[0]
        
        txs_status = koios_python.get_tx_status(["0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94",
                                                 "f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e"])
        assert 'code' not in txs_status[0]
'''