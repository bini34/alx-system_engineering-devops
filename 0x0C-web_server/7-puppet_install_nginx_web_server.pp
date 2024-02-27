# Puppet manifest to install and configure Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define default index file content
$file_content = "Hello World!"

# Ensure default index file exists and contains the specified content
file { '/var/www/html/index.html':
  ensure  => present,
  content => $file_content,
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
}

# Configure Nginx redirection
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}",
  notify  => Service['nginx'],
}
