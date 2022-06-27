# Web3 / Pense-bête

## Challenge
Agent, nous avons réalisé que l'essor de la blockchain ces dernières années a donné aux criminels de nouveaux moyens d'essayer de s'échapper de nos radars. Il est donc absolument nécessaire que nous ne soyons pas en retard sur ces dernières technologies sous peine de le payer cher.

Par conséquent, nous avons décidé de monter une équipe spécialisée dans l'univers du web3 et nous voudrions que vous en fassiez partie. Voici le kit de survie dont vous aurez besoin pour commencer votre apprentissage :
- Programmation: web3.py ou web3.js
- Endpoints: Infura est très utile pour obtenir ses premiers enpoints gratuitement
- Cours: Cours ludique pour découvrir solidity: cryptozombies

Hallebarde ne faisant pas exception, il semble qu'elle commence à déployer ses propres smart contracts de son côté. Nous avons trouvé un contrat de Hallebarde permettant de récupérer un de leurs mots de passe. Essayez de dérober cette information.
- Contrat à l'adresse: `0xB65E30DeD2cD7d5C4758082BACE737976F8b214B`
- Réseau de test Ropsten

Format du flag: 404CTF{{MotDePasse}

## Inputs
- Smart contract address: 0xB65E30DeD2cD7d5C4758082BACE737976F8b214B
- Ropsten test network
- Solidity file for the smart contract: [intro.sol](./intro.sol)

## Solution
Since I know nothing about smart contracts, I spent some time reading the suggested documentation. The starting point is the `Solidity file`, which shows that the contract `Password` contains a public field `password`:
```console
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
```

Since this is a public field, an API is automatically generated to access it: `c.functions.password().call()`.

So what we could do is:
- Compile the provided `Solidity file` using `solc`
- Get the `ABI` from the contract interface (from the compiled `Solidity file`)
- Get an endpoint for free on `Infura`, so we can access the contract on the `Ropsten` test network using the c`ontract address` and the `ABI`
- Call the `password().call()` API to get the public variable `password`

But before that, we need to install `solc` (the `Solidity compiler`) using:
```python
from solcx import install_solc
install_solc(version='0.8.13')
```

Here is the Python code:
```python
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
```

```console
$ python3 sol.py
M0N_M07_D3_P4553_357_7r0P_53CUr153_6r4C3_4_14_810CKCH41N
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{M0N_M07_D3_P4553_357_7r0P_53CUr153_6r4C3_4_14_810CKCH41N}
