# Create User 1
curl -X POST "http://localhost:8000/api/users" -H "Content-Type: application/json" -d '{
  "email": "user1@example.com",
  "password": "password1"
}'

# Create User 2
curl -X POST "http://localhost:8000/api/users" -H "Content-Type: application/json" -d '{
  "email": "user2@example.com",
  "password": "password2"
}'

# Create User 3
curl -X POST "http://localhost:8000/api/users" -H "Content-Type: application/json" -d '{
  "email": "user3@example.com",
  "password": "password3"
}'

# Create User 4
curl -X POST "http://localhost:8000/api/users" -H "Content-Type: application/json" -d '{
  "email": "user4@example.com",
  "password": "password4"
}'

# Create User 5
curl -X POST "http://localhost:8000/api/users" -H "Content-Type: application/json" -d '{
  "email": "user5@example.com",
  "password": "password5"
}'





# Create Role 1
curl -X POST "http://localhost:8000/api/roles" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGV4YW1wbGUuY29tIiwidXNlcl9pZCI6IjY2NWRhMDkwMTc2ZmRiMzgwMzZhN2Y4MSIsImV4cCI6MTcxNzQ1NTQ3NH0.QIsc0XDNLQT5nkaqbBjkgHsrPjb1In3Y2NNwVtU0oFo" -H "Content-Type: application/json" -d '{
  "role_name": "Owner",
  "permissions": ["create", "read", "update", "delete"]
}'

# Create Role 2
curl -X POST "http://localhost:8000/api/roles" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGV4YW1wbGUuY29tIiwidXNlcl9pZCI6IjY2NWRhMDkwMTc2ZmRiMzgwMzZhN2Y4MSIsImV4cCI6MTcxNzQ1NTQ3NH0.QIsc0XDNLQT5nkaqbBjkgHsrPjb1In3Y2NNwVtU0oFo" -H "Content-Type: application/json" -d '{
  "role_name": "Member",
  "permissions": ["read", "update"]
}'
curl -X POST "http://localhost:8000/api/login" -H "Content-Type: application/json" -d '{
  "email": "user1@example.com",
  "password": "password1"
}'



# Create Group
curl -X POST "http://localhost:8000/api/groups" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGV4YW1wbGUuY29tIiwidXNlcl9pZCI6IjY2NWRhMDkwMTc2ZmRiMzgwMzZhN2Y4MSIsImV4cCI6MTcxNzQ1NTQ3NH0.QIsc0XDNLQT5nkaqbBjkgHsrPjb1In3Y2NNwVtU0oFo" -H "Content-Type: application/json" -d '{
  "group_name": "Trip Group 1",
  "members": [
    {"user_id": "665da089176fdb38036a7f80", "role_id": "665da2b6b7ff4d3b3a1fd2a9"},
    {"user_id": "665da06d176fdb38036a7f7f", "role_id": "665da234b7ff4d3b3a1fd2a8"}
    {"user_id": "665da090176fdb38036a7f81", "role_id": "665da234b7ff4d3b3a1fd2a8"}
  ],
  "trip_ids": []
}'

# Trip create

 curl -X POST "http://localhost:8000/api/trips" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGV4YW1wbGUuY29tIiwidXNlcl9pZCI6IjY2NWRhMDkwMTc2ZmRiMzgwMzZhN2Y4MSIsImV4cCI6MTcxNzQ1NTQ3NH0.QIsc0XDNLQT5nkaqbBjkgHsrPjb1In3Y2NNwVtU0oFo" -H "Content-Type: application/json" -d '{
  "name": "Vacation to Hawaii",
  "location": "Hawaii, USA",
  "description": "A relaxing trip to Hawaii",
  "start_date": "2024-07-01",
  "end_date": "2024-07-10",
  "budget": 2000.0
}'

#Destination create

curl -X POST "http://localhost:8000/api/destinations" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGV4YW1wbGUuY29tIiwidXNlcl9pZCI6IjY2NWRhMDkwMTc2ZmRiMzgwMzZhN2Y4MSIsImV4cCI6MTcxNzQ1NTQ3NH0.QIsc0XDNLQT5nkaqbBjkgHsrPjb1In3Y2NNwVtU0oFo" \
-H "Content-Type: application/json" \
-d '{
  "trip_id": "665da874ece788e7314d4c95",
  "name": "Paris",
  "description": "A trip to Paris",
  "start_date": "2024-07-01",
  "end_date": "2024-07-05",
  "destination_type": "overnight stay",
  "suggestions": [{"name": "Eiffel Tower", "description": "Visit the Eiffel Tower"}]
}'

# Activity create
curl -X POST "http://localhost:8000/api/activities" \
-H "Authorization: Bearer your_access_token" \
-H "Content-Type: application/json" \
-d '{
  "name": "Hiking at Grand Canyon",
  "description": "Enjoy a breathtaking hike along the Grand Canyon trails.",
  "destination_id": "665dad7dc434a1a1bddcbf9c",
  "suggestions": [
    {"name": "Bring plenty of water"},
    {"name": "Wear comfortable hiking shoes"}
  ]
}'

