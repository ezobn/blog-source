Title: Juju - Automate your cloud infrastructure
Date: 2015-01-18 20:00
Category: Ubuntu 
Tags: Juju

Configure, manage, maintain, deploy and scale efficiently with best-practice Charms on any public, private or hybrid cloud from a powerful GUI or the command-line.
- Deploy
Juju manages your systems architecture as services in the cloud. It is a simple client/server application that bootstraps an instance to create and control the rest of your environment. You can use it through a GUI or from the command-line, scale in all directions and easily move your environment between clouds.
- Juju manages services
In modern scale out architectures, servers are just units that enable application services to scale. Services are managed independently of the underlying hardware so you don’t need to worry about launching new instances and setting up config files to connect applications, Juju just takes care of it all.
Other solutions focus on configuration management to enforce consistency across scale out architectures but Juju creates services as building blocks that are connected together simply by drawing a line between the two. It is this service based approach that allows dev-ops and architects to quickly be able to visualise, design, deploy and scale their application infrastructures far more easily than if they are stuck in the weeds with configuration management tools.
- Environment portability
Moving applications through a product development lifecycle can be challenging. Juju enables you to export and import application architectures so that you can reproduce the exact same environment at every stage.
Just as easily, you can move between all the different cloud platforms that Juju supports.
Design and test on your local host. Export a set of services from OpenStack and deploy them onto EC2 in seconds. Move from EC2 to Azure just as quickly. Juju lets you move your infrastructure between providers and even create hybrid structures without you having to worry about cloud APIs or protocols.
- Scale in all directions
Scale out, scale back. Adding or removing capacity from your infrastructure is as simple as a single click with Juju. For more sophistication, connect your monitoring application to Juju and launch or destroy capacity based on thresholds you determine. If you need extra performance offered on another cloud environment, you can easily migrate your workloads and take advantage of any technical or financial advantages on offer.
- Added intelligence with Landscape
For the highest levels of infrastructure automation you can use Landscape, Canonical’s systems management tool. Used in conjunction with Juju, Landscape is able to automate scaling, systems updates, security audits and compliance reporting to ensure that you can scale your operations in the most cost effective way possible. Together, Landscape and Juju create efficiency through intelligent automation.

![charms](https://juju.ubuntu.com/wp-content/uploads/2013/10/homepage-hero.png)

- Charms
Scalable application services defined
Charms give Juju its power. They encapsulate application configurations, define how services are deployed, how they connect to other services and are scaled. Charms are easily shared and there are 100s of Charms already rated and reviewed in our Charm store.

- Best practice built in
Juju is designed to encourage collaboration on the optimal ways to deploy, configure and connect applications to other services. Many Charms have had leading experts contribute — you benefit from their experience and knowledge.Charms are vetted and scored to help give you an indication of quality and the very best charms are featured on jujucharms.com

- Inside a Charm
Charms define how services integrate and how their service units react to events in the distributed environment, as orchestrated by Juju. Charms can be written in any language that runs on Ubuntu. To pull it altogether, you just need to create a simple metadata.yaml file that defines the Charms’ metadata, interfaces, hooks and requires.
[Learn more about the anatomy of a Charm ›](https://juju.ubuntu.com/docs/authors-charm-components.html)

- Customise existing Charms
Charms are written in a variety of languages although the majority are written as bash or python scripts. You can modify any existing Charm to suit your needs — pull files from internal repositories, set security or admin policy or anything else needed to make them fit your environment.

![Image](https://juju.ubuntu.com/wp-content/themes/ubuntu/library/images/juju-deployment-hero.png)