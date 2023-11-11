rem chrome : rem - is a comment command

pytest -s -v -m "sanity" --html=./Reports/report1.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/report1.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report1.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report1.html testCases/ --browser chrome