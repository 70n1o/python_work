import requests

from plotly.graph_objs import Bar
from plotly import offline
from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts, response_dicts = [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle:", submission_dict['title'])
    print(f"Discussion link:", submission_dict['link'])
    print(f"Comments:", submission_dict['comments'])


"""17-1. Other Languages: Modify the API call in python_repos.py so it generates
a chart showing the most popular projects in other languages. Try languages
such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.

17-2. Active Discussions: Using the data from hn_submissions.py, make a bar
chart showing the most active discussions currently happening on Hacker
News. The height of each bar should correspond to the number of comments
each submission has. The label for each bar should include the submission’s
title and should act as a link to the discussion page for that submission.

17-3. Testing python_repos.py: In python_repos.py, we printed the value of
status_code to make sure the API call was successful. Write a program called
test_python_repos.py that uses unittest to assert that the value of status_code
is 200. Figure out some other assertions you can make—for example, that the
number of items returned is expected and that the total number of repositories
is greater than a certain amount.

17-4. Further Exploration: Visit the documentation for Plotly and either the
GitHub API or the Hacker News API. Use some of the information you find
there to either customize the style of the plots we’ve already made or pull some
different information and create your own visualizations."""