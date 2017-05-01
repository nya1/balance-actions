# Balance Actions

Executes a script when the provided address reach the balance limit.

Cronjob is recommended for an automated check.

See a [general example](#example) or a [cronjob example](#cronjob-example)

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

```bash
python balance-actions.py 
	--address 0x0000000000000000000000000000000000000000
	--url-list http://localhost:8545 http://my.remote.eth.node.com https://pub-node26224.etherscan.io/
	--limit 2000000000000000000
	--script-path /home/user/refill_account.sh
```

Trigger `/home/user/refill_account.sh` if the account balance of `0x0000000000000000000000000000000000000000` is less than 2000000000000000000 wei (2 ether), using more than 1 node for backup.

**Please note:** The `--script-path` script file must be executable (`chmod +x <script>`)


### Cronjob example

Edit the crontab

```bash
crontab -e
```

Add a new cronjob, every 30 minutes the `balance-actions.py` script will be executed with the [custom options](#example).

```bash
*/30 * * * * /home/user/balance-actions/balance-actions.py <my-options>
```

**Please note:** `balance-actions.py` and the script that will be executed must be executable (`chmod +x <script>`)
