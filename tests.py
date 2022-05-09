#!/usr/bin/env python

# We need to install and import koios_python library
import koios_python
import pprint  # I recommend use pprint.pp to print the querys

#alternative if we just need some functions
#from koios_python import block, epochs

# Some examples:

# Get info of epoch number 338:
#print(koios_python.get_epoch_params(338))

# Get info of two transactions:
#print(koios_python.get_tx_metadata(["f144a8264acf4bdfe2e1241170969c930d64ab6b0996a4a45237b623f1dd670e" \
# ,"0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# Submit an already serialized transaction to the network from a binay file-system
#print(koios_python.submit_tx("signed.cbor"))

# Get number of confirmations of a list of hash transactions
#print(koios_python.get_tx_status(["b50d56706c07a3c11f21fbbca3da7a3754398acb38b91a38a36cbea5c895e02f" \
# ,"0b8ba3bed976fa4913f19adc9f6dd9063138db5b4dd29cecde369456b5155e94"]))

# Get address info - balance, associated stake address (if any) and UTxO set.
#print(koios_python.get_address_info("addr1qyp9kz50sh9c53hpmk3l4ewj9ur794t2hdqpngsjn3wkc5sztv9glpwt3frwrhdrltjaytc8ut2k4w6qrx3p98zad3fq07xe9g"))

# Get the full rewards history (including MIR) for a stake address, or certain epoch if specified
#print(koios_python.get_account_rewards("stake1u8jm3v2q8h46q485j8e8uxqmj33f4cy4xvadkuq5g2c27ls44jflg" \
# ,335))

# Get the mint/burn history of an asset
#print(koios_python.get_asset_history("d3501d9531fcc25e3ca4b6429318c2cc374dbdbcf5e99c1c1e5da1ff" \
# , "444f4e545350414d"))

# Current pool statuses and details for a specified list of pool ids
#pprint.pp(koios_python.get_pool_info(["pool100wj94uzf54vup2hdzk0afng4dhjaqggt7j434mtgm8v2gfvfgp", \
#"pool102s2nqtea2hf5q0s4amj0evysmfnhrn4apyyhd4azcmsclzm96m", \
#"pool102vsulhfx8ua2j9fwl2u7gv57fhhutc3tp6juzaefgrn7ae35wm"]))

# Get the Pool List from the record 2001 to 3000
#pprint.pp(koios_python.get_pool_list("2001-3000"))

# List of all redeemers for a given script hash.
#print(koios_python.get_script_redeemers("d8480dc869b94b80e81ec91b0abe307279311fe0e7001a9488f61ff8"))
