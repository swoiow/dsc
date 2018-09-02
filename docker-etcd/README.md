## Ref
[github](https://github.com/coreos/etcd)

[repository](https://quay.io/repository/coreos/etcd?tab=tags)

## Doc
```
docker pull quay.io/coreos/etcd

docker run -it --rm --name etcd \
    -p 2379:2379 \
    -p 2380:2380 \
    -e NODE1=10.30.1.18 \
    quay.io/coreos/etcd:latest \
    /usr/local/bin/etcd \
    --data-dir=/etcd-data --name node1 \
    --initial-advertise-peer-urls http://$NODE1:2380 --listen-peer-urls http://0.0.0.0:2380 \
    --advertise-client-urls http://$NODE1:2379 --listen-client-urls http://0.0.0.0:2379 \
    --initial-cluster node1=http://$NODE1:2380
```