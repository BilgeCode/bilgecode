Mac OSX
=======

Start Here:
https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/#macosx

$ brew install postgresql
$ brew install postgis
$ brew install gdal
$ brew install libgeoip

postgres -D /usr/local/var/postgres

run these commands on your db (as the django user for permissions):

psql bc -c "CREATE EXTENSION postgis;"
psql bc -c "CREATE EXTENSION postgis_topology;"

test it:

$ psql -d <database_name> -c "select PostGIS_full_version()"

Ubuntu
======

install
http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS20Ubuntu1204

setup
http://blog.iiilx.com/programming/how-to-install-postgres-on-ubuntu-for-django/

