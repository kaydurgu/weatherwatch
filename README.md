## Models

### UserProfile

- **Fields:**
  - `username`: CharField (max_length=150, unique)
  - `email`: CharField (max_length=254, unique)
  - `phone_number`: CharField (max_length=20, blank=True, null=True)
  - `first_name`: CharField (max_length=30)
  - `last_name`: CharField (max_length=30)
  - `birth_date`: DateField (blank=True, null=True)
  - `address`: CharField (max_length=255, blank=True, null=True)
  - `hire_date`: DateField (blank=True, null=True)
  - `bio`: TextField (blank=True, null=True)
  - `is_active`: BooleanField (default=True)
  - `role`: CharField (max_length=10, choices=ROLE_CHOICES, default='worker')
  - `groups`: ManyToManyField (`auth.Group`, verbose_name='groups', blank=True, related_name='custom_user_groups')
  - `user_permissions`: ManyToManyField (`auth.Permission`, verbose_name='user permissions', blank=True, related_name='custom_user_permissions')

- **Choices:**
  - `ROLE_CHOICES`:
    - 'staff': 'Staff'
    - 'admin': 'Admin'

- **Methods:**
  - `__str__()`: Returns the username of the user.

- **Meta Options:**
  - `verbose_name`: "User"
  - `verbose_name_plural`: "Users"


### Sensor

- **Fields:**
  - `id`: AutoField (Primary Key)
  - `name`: CharField (max_length=100)
  - `type`: CharField (max_length=20, choices=SENSOR_TYPES, default='thermometer')
  - `model`: CharField (max_length=100)
  - `region`: CharField (max_length=20, choices=SENSOR_LOCATION_CHOICES, default='bishkek')
  - `location`: CharField (max_length=100)
  - `installation_date`: DateField (null=True, blank=True)
  - `status`: CharField (max_length=20, choices=SENSOR_STATUS_CHOICES, default='active')
  - `responsible`: ForeignKey (UserProfile, on_delete=models.CASCADE, null=True, blank=True)
  - `description`: TextField (null=True, blank=True)
  - `timestamp`: DateTimeField (auto_now_add=True)

- **Choices:**
  - `SENSOR_STATUS_CHOICES`: 
    - 'active': 'Active'
    - 'inactive': 'Inactive'
    - 'maintenance': 'Under Maintenance'
  - `SENSOR_LOCATION_CHOICES`: 
    - 'batken': 'Batken'
    - 'bishkek': 'Bishkek'
    - 'osh': 'Osh'
  - `SENSOR_TYPES`: 
    - 'thermometer': 'Thermometer'
    - 'hygrometer': 'Hygrometer'
    - 'barometer': 'Barometer'
    - 'wind_vane': 'Wind Vane'
    - 'snow_gauge': 'Snow Gauge'

- **Methods:**
  - `__str__()`: Returns the name of the sensor.

### Data

The `Data` model represents the data collected by a sensor. It includes fields to store various types of measurements such as temperature, humidity, pressure, wind speed, and wind direction.

- **Fields:**
  - `sensor`: ForeignKey (Sensor, on_delete=models.CASCADE, related_name='data')
  - `temperature`: FloatField (null=True, blank=True)
  - `humidity`: FloatField (null=True, blank=True)
  - `pressure`: FloatField (null=True, blank=True)
  - `wind_speed`: FloatField (null=True, blank=True)
  - `wind_direction`: CharField (max_length=250, blank=True, null=True)

- **Methods:**
  - `__str__()`: Returns a string indicating the data belongs to which sensor.

### Alert

The `Alert` model represents alerts related to a sensor. It includes fields to store the description of the alert, the severity, the last timestamp when it was updated, and notes.

- **Fields:**
  - `sensor`: ForeignKey (Sensor, on_delete=models.CASCADE, related_name='alerts')
  - `description`: TextField
  - `last_timestamp`: DateTimeField (auto_now=True)
  - `last_timecheckedby`: ForeignKey (UserProfile, on_delete=models.CASCADE)
  - `warning_notes`: TextField (null=True, blank=True)
  - `severity`: CharField (max_length=10, choices=SENSOR_SEVERITY_CHOICES, default='ok')

- **Choices:**
  - `SENSOR_SEVERITY_CHOICES`: 
    - 'high': 'High'
    - 'medium': 'Medium'
    - 'low': 'Low'
    - 'ok': 'Ok'

## API Endpoints

### Users

- `GET /users/`: List all users (requires authentication).
- `GET /users/auth/`: Authentication endpoint.
- `GET /users/<int:pk>/`: Retrieve a user by ID (requires authentication).
- `PUT /users/update/<int:pk>/`: Update a user by ID (requires authentication and admin permissions).
- `POST /users/create/`: Create a new user (requires authentication and admin permissions).
- 
### Sensors

- `GET /sensors/`: List all sensors (requires staff group).
- `GET /sensors/<int:pk>/`: Retrieve a sensor by ID (requires staff group).
- `PUT /sensors/update/<int:pk>/`: Update a sensor by ID (requires admin group).
- `GET /sensors/active/`: List all active sensors.
- `GET /sensors/inactive/`: List all inactive sensors.
- `GET /sensors/inmaintenance/`: List all sensors under maintenance.
- `GET /sensors/data/<int:pk>/`: Retrieve data for a sensor by ID.
- `PUT /sensors/data/update/<int:pk>/`: Update data for a sensor by ID.
- `GET /sensors/alert/<int:pk>/`: Retrieve alerts for a sensor by ID.
- `PUT /sensors/alert/update/<int:pk>/`: Update alerts for a sensor by ID.
- `GET /sensors/alerts/`: List all alerts for sensors.
