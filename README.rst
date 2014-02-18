========
Roadtrip
========

Route53 domain updates for humans named Matt. At least it works for him. You might find it useful too.

Installation
============

With pip::

	$ pip install roadtrip

With setuptools::

	$ easy_install roadtrip

Requirements
============

Roadtrip requires `Python 2.7 <http://www.python.org>`_ and leans heavily on the shoulders of `Boto 2.25.0+ <http://boto.readthedocs.org>`_.

Using
=====

You can use roadtrip to update a round-robin A record, adding a new value if it doesn't already exist::

	$ roadtrip --type A --zone example.com --name mycluster.example.com --value 1.2.3.4 --add

There is also a compact syntax for each option::

	$ roadtrip -t A -z example.com -n mycluster.example.com -v 1.2.3.4 -a

You can also remove a value from a list::

	$ roadtrip --type A --zone example.com --name mycluster.example.com --value 1.2.3.4 --delete

You can also get help::

	$ roadtrip -h
	usage: roadtrip [-h] --type {A,AAAA,CNAME,MX,NS,PTR,SOA,SPF,SRV,TXT} --zone
	                ZONE --name NAME --value VALUE [--ttl TTL] (--add | --delete)
	                [--access-key ACCESS_KEY] [--secret-key SECRET_KEY]
	                [--verbose]

	Update a Route53 record, adding or removing values.

	optional arguments:
	  -h, --help            show this help message and exit
	  --type {A,AAAA,CNAME,MX,NS,PTR,SOA,SPF,SRV,TXT}, -t {A,AAAA,CNAME,MX,NS,PTR,SOA,SPF,SRV,TXT}
	                        The type of record to update.
	  --zone ZONE, -z ZONE  The domain name or zone ID.
	  --name NAME, -n NAME  The name to update.
	  --value VALUE, -v VALUE
	                        The data to add or remove.
	  --ttl TTL, -l TTL     Non-default TTL value.
	  --add, -a             Add the value.
	  --delete, -d          Remove the value.
	  --access-key ACCESS_KEY, -k ACCESS_KEY
	                        Your AWS access key. Will override the
	                        AWS_ACCESS_KEY_ID environment variable.
	  --secret-key SECRET_KEY, -s SECRET_KEY
	                        Your AWS secret key. Will override the
	                        AWS_SECRET_ACCESS_KEY envionrment variable.
	  --verbose, -vv        Verbose output.


You can set a non-default TTL value with ``--ttl`` and enable verbose output with ``--verbose``.

Roadtrip will use the ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY`` environment variables if they are set. You
can provide these values yourself or override the environment variables by providing ``--access-key`` and ``--secret-key``.

Under the hood
==============

Roadtrip will do its best not to add an entry that already exists or delete an entry that doesn't. It uses
`UPSERT <http://aws.typepad.com/aws/2014/01/new-features-for-route-53-improved-health-checks-https-record-modification.html>`_
to update the values based on the values that exist when you call it.

.. WARNING::

	Due to the nature of eventual consistency there is a chance that the values that roadtrip sees when it is run
	are different than the values stored in Route53. **ROADTRIP MIGHT HELP YOU LOSE DATA** if you are not careful.
	Please be careful.
