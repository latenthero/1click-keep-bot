bot_token = 'TOKEN'
log_name = '1click_keep_bot.log'
commands = [
    "sudo apt update",
    "sudo apt install docker.io curl git -y",
    "sudo systemctl start docker",
    "sudo systemctl enable docker",
    "sudo ufw allow 3919 && sudo ufw allow 3920",
    "sudo ufw status",

    "git clone https://github.com/icohigh/keep-nodes.git",
    "echo '%s' >> $HOME/keep-nodes/data/eth-address.txt && echo '%s' >> $HOME/keep-nodes/data/eth-address-pass.txt && echo '%s' >> $HOME/keep-nodes/data/keep_wallet.json",
    "echo 'export ETH_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt)' >> $HOME/.profile",
    "echo 'export SERVER_IP=$(curl ifconfig.co)' >> $HOME/.profile",
    "grep -rl INFURA_BEACON_ID $HOME/keep-nodes/beacon/config* | xargs perl -p -i -e 's/INFURA_BEACON_ID/df8574df74084c71a997f56f137562d0/g'",
    "grep -rl INFURA_ECDSA_ID $HOME/keep-nodes/ecdsa/config* | xargs perl -p -i -e 's/INFURA_ECDSA_ID/ab706352c72543af96db73d3b38edad4/g'",
    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/beacon/config/config.toml",
    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/beacon/config/config.toml",
    "sed -i 's/.*URL = .*/URL = \"wss:\/\/ropsten.pfk2020.top\/wss\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
    "sed -i 's/.*URLRPC = .*/URLRPC = \"https:\/\/ropsten.pfk2020.top\/rpc\"/g' $HOME/keep-nodes/ecdsa/config/config.toml",
    "sudo docker run -d \
        --entrypoint /usr/local/bin/keep-client \
        --restart always \
        --volume $HOME/keep-nodes/data:/mnt/data \
        --volume $HOME/keep-nodes/beacon/config:/mnt/beacon/config \
        --volume $HOME/keep-nodes/beacon/persistence:/mnt/beacon/persistence \
        --env KEEP_ETHEREUM_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt) \
        --env LOG_LEVEL=debug \
        --name keep-client \
        -p 3919:3919 \
        keepnetwork/keep-client:v1.3.0-rc.4 --config /mnt/beacon/config/config.toml start",
    "sudo docker run -d \
        --entrypoint /usr/local/bin/keep-ecdsa \
        --restart always \
        --volume $HOME/keep-nodes/data:/mnt/data \
        --volume $HOME/keep-nodes/ecdsa/config:/mnt/ecdsa/config \
        --volume $HOME/keep-nodes/ecdsa/persistence:/mnt/ecdsa/persistence \
        --env KEEP_ETHEREUM_PASSWORD=$(cat $HOME/keep-nodes/data/eth-address-pass.txt) \
        --env LOG_LEVEL=debug \
        --name keep-ecdsa \
        -p 3920:3919 \
        keepnetwork/keep-ecdsa-client:v1.2.0-rc.5 --config /mnt/ecdsa/config/config.toml start"
            ]
