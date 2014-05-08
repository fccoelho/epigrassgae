Epigrass Web platform
=====================

The Epigrass web platform is an online platoform for sharing Epigrass based models and its simulation results.

The models need to be built and simulated in Epigrass, and then uploaded to the site.

[Go to the website](http://app.epigrass.net)

What is Epigrass?
---------------------
It is a free software project for the simulation of geo-referenced network models.

What makes this Boilerplate Amazing?
------------------------------------
It is fully featured, actively maintained, and uses the latest and most supported technologies of Google App Engine.

New to Google App Engine? Learn about it by watching [this video](http://www.youtube.com/watch?v=bfgO-LXGpTM) or reading [this website](https://developers.google.com/appengine/).

Get started in just a few easy steps
------------------------------------
1. Download the last version of the [App Engine SDK](http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python) for Linux, Mac OS or Windows (Tested with SDK version 1.7.2).
1. Download the code of this Boilerplate ([here](https://github.com/coto/gae-boilerplate/zipball/master))
1. Run locally ([instructions](https://developers.google.com/appengine/docs/python/tools/devserver)).
1. Set your 'application' name in [app.yaml](https://github.com/coto/gae-boilerplate/blob/master/app.yaml)
1. Set custom config parameters in [config/localhost.py](https://github.com/coto/gae-boilerplate/blob/master/config/localhost.py).  (secret key, [recaptcha code](http://www.google.com/recaptcha/whyrecaptcha), salt etc.)  To get started, copy the default settings from [boilerplate/config.py](https://github.com/coto/gae-boilerplate/blob/master/boilerplate/config.py). . Note that most of the default settings will need to be changed to yield a secure and working application.  Make the changes to these settings in the config/*.py (localhost.py for development on your local PC, production.py for production on App Engine's servers, testing.py for unittests configurations)  The configurations in /config take precedence over boilerplate/config.py.
1. Set Authentication Options dropdown to Federated Login in the Google App Engine control panel (or if you do not want federated login, set enable_federated_login to false in config.py)
1. Deploy it online ([instructions](https://developers.google.com/appengine/docs/python/gettingstarted/uploading) - recommended setup: python 2.7, high replication datastore)

