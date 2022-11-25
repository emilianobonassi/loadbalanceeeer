# Loadbalanceeeer

PoC local JSON-RPC load-balancer with opt-in anonymizer via Tor

## Why

Distribute RPC requests across different RPC providers and eventually use a proxy for privacy purposes

## How use it

- Install [Docker](https://docs.docker.com/get-docker/)

- Clone the repo

- Edit `rpc.txt` with your RPCs (currently some public examples from [Ethereum Nodes](https://ethereumnodes.com/))

- For only load balancing, run `docker-compose up -f docker-compose.yml`

- For more privacy, run `docker-compose up -f docker-compose.yml -f docker-compose.proxy.yml`

- You get your new RPC at `http://localhost:9545`

## Architecture

Only Load Balancing

```
                            => remote_rpc_1
                           |
user => (localhost:9545) -     ...
                           |
                            => remote_rpc_N
```

With Anonymizer/Proxy

```
                                         => remote_rpc_1
                                        |
user => (localhost:9545) => (tor/proxy) -     ...
                                        |
                                         => remote_rpc_N
```

## Disclaimer

This is only to demonstrate how to load balance request across multiple providers and how tunnel them via a proxy for analysis, debugging (e.g. mitmproxy) and privacy purposes. 

Use at your own risks.