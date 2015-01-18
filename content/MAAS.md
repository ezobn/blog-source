Title: MAAS - Metal as a Service 
Date: 2015-01-18 17:00
Category: Ubuntu 
Tags: MAAS

Metal as a Service brings the language of the cloud to physical servers. It makes it easy to set up the hardware on which to deploy any service that needs to scale up and down dynamically; a cloud being just one example.

It lets you provision your servers dynamically, just like cloud instances – only in this case, they’re whole physical nodes. “Add another node to the Hadoop cluster, and make sure it has at least 16GB RAM” is as easy as asking for it.

![MAAS architecture](http://maas.ubuntu.com/docs1.5/_images/orientation_architecture-diagram.png)

MAAS is designed to work with your physical hardware, whether your setup includes thousands of server boxes or only a few. The key components of the MAAS software are:

- Region controller
- Cluster controller(s)
- Nodes

For small (in terms of number of nodes) setups, you will probably just install the Region controller and a cluster controller on the same server - it is only worth having multiple region controllers if you need to organise your nodes into different subnets (e.g. if you have a lot of nodes).

With a simple web interface, you can add, commission, update and recycle your servers at will. As your needs change, you can respond rapidly, by adding new nodes and dynamically re-deploying them between services. When the time comes, nodes can be retired for use outside the MAAS.

MAAS works closely with the service orchestration tool  [Juju](http://juju.ubuntu.com/) to make deploying services fast, reliable, repeatable and scalable.