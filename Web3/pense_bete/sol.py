from web3 import Web3, HTTPProvider
from solcx import compile_source

compiled_sol = compile_source(
    '''
    pragma solidity 0.8.13;

    contract Password {

        string public password;

        constructor(string memory _password) public {
            password = _password;
        }

        function isPassword(string memory _password) external view returns (bool) {
            return (keccak256(abi.encodePacked((password))) == keccak256(abi.encodePacked((_password))));
        }

    }
    '''
    ,
    output_values = ['abi', 'bin']
)

contract_id, contract_interface = compiled_sol.popitem()
byte_code = contract_interface['bin']
abi = contract_interface['abi']

w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/db2a909bbc7c43dbb5684a5432255963"))
c = w3.eth.contract(address='0xB65E30DeD2cD7d5C4758082BACE737976F8b214B',abi=abi)
p = c.functions.password().call()
print(p)
