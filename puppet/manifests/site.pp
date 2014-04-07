# Use this file to add stuff required only on the development
#   environement. 
# Example: database creation and configuration (usually)
#
# Anything required on both (development and production)
#   environments should be placed on the {{ project_name }}
#   module instead of here.

include {{ project_name }}


### MySQL example:
#
# class { 'mysql::server':
#   override_options => {
#     mysqld => {
#       "default-storage-engine" => 'InnoDB',
#     },
#   },
# }
#
# mysql::db { '{{ project_name }}':
#   user     => '{{ project_name }}',
#   password => '{{ project_name }}',
#   host     => 'localhost',
#   grant    => ['ALL'],
#   charset  => 'utf8',
# }


### PostgreSQL example:
#
# include postgresql::server
#
# postgresql::server::db { '{{ project_name }}':
#   user     => '{{ project_name }}',
#   password => '{{ project_name }}',
# }
