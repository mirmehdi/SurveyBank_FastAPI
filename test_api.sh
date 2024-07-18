#!/bin/bash

# Test getting questions
echo "Testing GET /questions"
curl -u alice:wonderland -X GET "http://127.0.0.1:8000/questions?use=Test%20de%20positionnement&subjects=BDD&count=5" -H "accept: application/json"
echo ""

# Test adding a question
echo "Testing POST /questions"
curl -u admin:4dm1N -X POST "http://127.0.0.1:8000/questions" -H "accept: application/json" -H "Content-Type: application/json" -d '{
  "question": "New question?",
  "subject": "Math",
  "correct": "A",
  "use": "test",
  "responseA": "Option A",
  "responseB": "Option B"
}'
echo ""

