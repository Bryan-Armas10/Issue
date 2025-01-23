Mini Challenge 3

Issue management MVP

User story 1

As a product owner, I would like to be able to create issues, so that developers may conduct work on them.

Acceptance Criteria

1.-An issue must contain, at a minimum, the following fields:
1.1. name
1.2. summary
1.3. description
1.4. reporter (foreign key to user)
1.5. assignee (can be null, foreign key to user)
1.6. status (can be "to do", "in progress" or "done")
1.7. created on (date time)
1.8. priority level (can be low, medium or high)

2.-Make sure priorities and statuses are available as a result of one or more migrations.


User story 2

As a developer, I would like to be able to update the status of an issue (or task) so that I can represent the work I am doing on the board.

Acceptance Criteria

1.-Add full CRUDS support to the Issue model, ensuring that:
1.1. Tasks can be seen on a board view, organized by status.
1.2. Only product owners can create new issues.
1.3. Only developers can update an issue's status.
1.4. For now: nobody can delete an issue, we'll cover that later.
1.5. A detail view shows all the fields related to an issue.

2.-Test.

===============================================================
if self.request.user.role.name == “product owner”:

    return True

else:

   return False