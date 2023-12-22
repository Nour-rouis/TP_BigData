import sys

# Initialize variables
current_url = None
total_page_views = 0
url = None

for line in sys.stdin:
    line = line.strip()

    url, count = line.split("\t", 1)

    try:
        page_views = int(count)
    except ValueError:
        continue

    if current_url == url:
        total_page_views += page_views
    else:
        if current_url is not None:
            # emit the total page views for the current URL
            print('{}\t{}'.format(current_url, total_page_views))

        current_url = url
        total_page_views = page_views

# Print the result for the last URL
if current_url is not None:
    print('{}\t{}'.format(current_url, total_page_views))
