========
Roadtrip
========

Roadtrip: Route53 domain updates for humans named Matt. At least it works for him. You might find it useful too.

Installation
============

With pip::

	$ pip install roadtrip

With setuptools::

	$ easy_install roadtrip

Using
=====

You can use roadtrip to update a round-robin A record, adding a new value if it doesn't already exist::

	$ roadtrip --type A --zone tinygophers.com --name serf1.tinygophers.com --value 1.2.3.4 --add

There is also a compact syntax for each option::

	$ roadtrip -t A -z tinygophers.com -n serf1.tinygophers.com -v 1.2.3.4 -a

You can also remove a value from a list::

	$ roadtrip --type A --zone tinygophers.com --name serf1.tinygophers.com --value 1.2.3.4 --delete

You can also get help::

	$ roadtrip -h

Under the hood
==============

Roadtrip will do its best not to add an entry that already exists or delete an entry that doesn't. It uses
`UPSERT <http://aws.typepad.com/aws/2014/01/new-features-for-route-53-improved-health-checks-https-record-modification.html>`_
to update the values based on the values that exist when you call it.

.. WARNING::

	Due to the nature of eventual consistency there is a chance that the values that roadtrip sees when it is run
	are different than the values stored in Route53. **ROADTRIP MIGHT HELP YOU LOSE DATA** if you are not careful.
	Please be careful.
