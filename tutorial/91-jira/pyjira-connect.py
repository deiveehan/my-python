from jira import JIRA


jira = JIRA(server="https://jira-cmdspace.atlassian.net", basic_auth=('deiveehan@gmail.com', 'VjqefqNKep9CZGVfmb5X8814'))


myself = jira.myself()
boards = jira.boards()
print(boards)

issues_in_proj = jira.search_issues('project=FUDY')

# my top 5 issues due by the end of the week, ordered by priority
oh_crap = jira.search_issues('assignee = currentUser() and due < endOfWeek() order by priority desc', maxResults=5)

# Summaries of my last 3 reported issues
for issue in jira.search_issues('project=FUDY and reporter = currentUser() order by created desc', maxResults=5):
    print('{}: {}'.format(issue.key, issue.fields.summary))
    # print(issue.fields.issuetype.name)

