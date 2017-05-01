# Balance Actions

Automatically executes a script when the provided address reach the balance limit

___


Tested on Python 2.7 and 3

`python balance-actions.py <options>`

```
  -h, --help            show this help message and exit
  --url URL             http node
  --url-list URL_LIST [URL_LIST ...]
                        http node list (N+1 is a backup node)
  --address ADDRESS     address to watch for
  --script-path SCRIPT_PATH
                        script location (full path)
  --limit LIMIT         balance limit (in wei)

```

### Example

```
python balance-actions.py 
	--address 0x0000000000000000000000000000000000000000
	--url-list http://localhost:8545 http://my.remote.eth.node.com https://pub-node26224.etherscan.io/
	--limit 2000000000000000000
	--script-path /home/user/refill_account.sh
```

Trigger `/home/user/refill_account.sh` when the account balance of `0x0000000000000000000000000000000000000000` is less than 2000000000000000000 wei (2 ether), using more than 1 node for backup.
