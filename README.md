# Web Wrapper for PittAPI
[![Build Status](https://travis-ci.org/Pitt-CSC/PittAPIWebWrapper.svg?branch=master)](https://travis-ci.org/Pitt-CSC/PittAPIWebWrapper)
[![License GPLv2](https://img.shields.io/badge/license-GPLv2-blue.svg)](LICENSE)
![Python 3.4, 3.5](https://img.shields.io/badge/python-3.4%2C%203.5-green.svg)

# Installation
1. Clone this repo
1. Create a virtual environment `virtualenv venv` and enable it. `source venv/bin/activate`
1. Run `pip install -r requirements.txt` to install dependencies.
1. Launch `python server.py` to run the server.

# API Endpoints

#### Courses
```
/courses/<term>/<code>
```

#### Classes
```
/class/<class_number>/<term>
```

#### Lab Status
```
/lab_status/<lab_name>
```

#### Laundry Status
For simple laundry status:
```
/laundry/simple/<location>
```

For detailed laundry status:
```
/laundry/detailed/<location>
```

#### People
```
/people/<query>
```

#### Shuttles
For shuttle routes:
```
/shuttle/routes
```

For shuttle vehicle points:
```
/shuttle/points
```

For shuttle arrivals:
```
/shuttle/arrivals/<times_per_stop>
```

For shuttle stop estimates:
```
/shuttle/estimates/<vehicle_id>/<quantity>
```

#### Textbooks
If the term is to be specified:
```
/textbook/<department_code>/<course_name>/<instructor>/<term>
```

If the term is not to be specified:
```
/textbook/<department_code>/<course_name>/<instructor>
```

#### News
```
/news/<feed>/<max_news_items>
```


## License
```
Web Wrapper for PittAPI, web app for REST endpoints for the PittAPI
Copyright (C) 2015 Ritwik Gupta

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
```
