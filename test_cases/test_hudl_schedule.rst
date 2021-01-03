##########################
Hudl Challenge - Part B
##########################

This file includes a set of detailed test cases for the schedule functionality of https://www.hudl.com .

==========================
Test cases
==========================

Each test case below explains the behavior between what the coach might see and how the data is being retrieved from a
backend service.

----------------------------
Test Success - View schedule
----------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to see its scheduled games.

When the coach accesses https://www.hudl.com/schedule the page should show a loading sign to the coach as well as trigger
a request to the backend in order to retrieve the data.

Request:

* Method: **GET**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side

Response:

* Status Code: **200 OK**
* Headers
    1. **session-id** - The validated session id
* Body::

    Example of expected response JSON:
    [
        {
            gameId: "0000001",

            sqlId: "0000001",

            date: "2021-01-01T15:00:00",

            opponent: "Opponent1",

            opponentId: "000001",

            isHome: true,

            gameType: 0,

            categories: [ ]
        }
    ]

Once the page receives the response it should read the JSON received on the response and create a list with an entry for
each schedule information on the JSON, as well as remove the loading sign from the screen.

The coach should then be able to see all its scheduled games as well as the options to remove or edit an existent
schedule and add new ones.

--------------------------------------------
Test Success - View schedule with no entries
--------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to see it's scheduled
games but it won't have any saved on the database.

When the coach accesses https://www.hudl.com/schedule the page should show a loading sign to the coach as well as trigger
a request to the backend in order to retrieve the data.

Request:

* Method: **GET**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side

Response:

* Status Code: **200 OK**
* Headers
    1. **session-id** - The validated session id
* Body::

    Example of expected response JSON:
    []

Once the page receives the response it should remove the loading sign from the screen and display a message to the coach
informing that no scheduled games were found.
For example: No schedule entries were found, please add a new one.

The coach should then be able to see an add button to add a new entry on the database.

-------------------------------------------------
Test Failure - View schedule returns unauthorized
-------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to see it's scheduled
games but its session ID expired so the requests can't be fulfilled.

When the coach accesses https://www.hudl.com/schedule the page should show a loading sign to the coach as well as
trigger a request to the backend in order to retrieve the data.

Request:

* Method: **GET**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A *invalid* session id to be validated on the backend side

Response:

* Status Code: **401 UNAUTHORIZED**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it informs the coach that its session is not valid so the operation couldn't
be completed.
For example: "Your session is not valid anymore, please refresh the page or login again."

---------------------------------------------
Test Failure - View schedule invalid coach ID
---------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to see its
scheduled games but the page requested the schedules to an invalid coachID.

When the coach accesses https://www.hudl.com/schedule the page should show a loading sign to the coach as well as trigger
a request to the backend in order to retrieve the data.

Request:

* Method: **GET**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - An *invalid* coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side

Response:

* Status Code: **404 NOT FOUND**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should remove the loading sign from the screen and display a message to
the coach informing that something went wrong whilst trying to retrieve its scheduled games.
For example: No schedule entries were found for this specific coachID.

The coach should then be able to see a retry button that will trigger the same request with the same parameters
again.

--------------------------------------------------
Test Failure - View schedule with unexpected error
--------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to see it's scheduled
games but the backend has trouble processing the request and returns an unexpected error.

When the coach accesses https://www.hudl.com/schedule the page should show a loading sign to the coach as well as trigger
a request to the backend in order to retrieve the data.

Request:

* Method: **GET**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side

Response:

* Status Code: **500 INTERNAL SERVER ERROR**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should remove the loading sign from the screen and display a message to
the coach informing that something went wrong whilst trying to retrieve its scheduled games.
For example: Something went wrong on our side please try again.

The coach should then be able to see a retry button that will trigger the same request with the same parameters
again.

----------------------------
Test Success - Edit schedule
----------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one or multiple
of its scheduled games.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished editing the information and clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **204 NO CONTENT**
* Headers
    1. **session-id** - The validated session id
    2. **ETag** - Tag to identify the specific version of this entry after the backend performed operations on it
* Body: **Empty**

Once the page receives the response it should compare the ETAG from the request and response and when both are
different inform the user that the entry was updated with success and send the new information on the edit
screen to the screen with the list of scheduled games so it can be updated.

The coach should then be able to see all its scheduled games plus the updated entry with the new values as well
as the options to remove or edit an existent schedule and add new ones.

------------------------------------------------------
Test Success - Edit schedule when data is not modified
------------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one of its
scheduled games but end up not changing any data before it presses save.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

Without changing anything on the screen the coach clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **204 NO CONTENT**
* Headers
    1. **session-id** - The validated session id
    2. **ETag** - Tag to identify the specific version of this entry after the backend performed operations on it
* Body: **Empty**

Once the page receives the response it should compare the ETag from the request and response and when both are
the same information the user that the nothing changed on that entry and go back to the screen with the list of
scheduled games.

-------------------------------------------------
Test Failure - Edit schedule returns unauthorized
-------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one or
multiple of its scheduled games but its session ID is not valid to fulfill the requests.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished editing the information and clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - An *invalid* session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **401 UNAUTHORIZED**
* Headers
    1. **session-id** - The validated session id
    2. **ETag** - Tag to identify the specific version of this entry after the backend performed operations on it
* Body: **Empty**

Once the page receives the response it informs the coach that its session is not valid so the operation couldn't
be completed.
For example: "Your session ID is not valid anymore, please refresh the page or login again."

-----------------------------------------------
Test Failure - Edit schedule with an empty body
-----------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one or
multiple of its scheduled games but the page sends the request without the JSON on the body.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished editing the information and clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body: **Empty**

Response:

* Status Code: **400 BAD REQUEST**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the user that the operation wasn't successful.
For example: Something happened and we weren't able to finish this operation.

The coach should then be given the option to try again, which will trigger the same request with the same
parameters again or go back to editing and change something else.

--------------------------------------------------
Test Failure - Edit schedule with an invalid value
--------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one or
multiple of its scheduled games but the page sends the request with a JSON containing invalid values in some fields.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished editing the information and clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "INEXISTENT_OPPONENT_ID",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **404 NOT FOUND**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the user that the operation wasn't successful.
For example: Something happened and we weren't able to finish this operation.

The coach should then be given the option to try again, which will trigger the same request with the same
parameters again or go back to editing and change something else.

------------------------------------------------
Test Failure - Edit schedule with missing fields
------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one or multiple
of its scheduled games but the page sends the request with the JSON missing some fields.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished editing the information and clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body::

    Example of expected request JSON missing "opponentId" field:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **422 UNPROCESSABLE ENTITY**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the user that the operation wasn't successful.
For example: Some of the data sent couldn't be processed please double-check and retry.

The coach should then be given the option to try again, which will trigger the same request with the same
parameters again or go back to editing and change something else.

--------------------------------------------------
Test Failure - Edit schedule with unexpected error
--------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to edit one or
multiple of its scheduled games but the backend has trouble processing the request and returns an unexpected error.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
edit one or more of the existent entries by clicking on the edit button.

Once the coach clicks the edit button a new screen should appear with fields filled with the information of that
specific entry and a save button. An example of the fields on the edit screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished editing the information and clicks the save button it triggers a request to the backend in
order to update the entry.

Request:

* Method: **PUT**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - An *invalid* session id to be validated on the backend side
    2. **ETag** - Tag to identify the specific version of this entry
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **500 INTERNAL SERVER ERROR**
* Headers
    1. **session-id** - The validated session id
    2. **ETag** - Tag to identify the specific version of this entry after the backend performed operations on it
* Body: **Empty**

Once the page receives the response it should inform the coach that something went wrong whilst trying to update the entry.
For example: Something went wrong on our side please try again.

The coach should then be able to see a retry button that will trigger the same request with the same parameters
again.

--------------------------------
Test Success - Create a schedule
--------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to add a new schedule entry.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
add a new entry by clicking on the create button.

Once the coach clicks the create button a new screen should appear with dropboxes filled with valid information,
the rest of the fields blank and a create button. An example of the fields on the create screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished filling the fields and clicks the create button it triggers a request to the backend in
order to create the entry.

Request:

* Method: **POST**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **201 OK**
* Headers
    1. **session-id** - The validated session id
* Body::

    Example of expected response JSON:
    {
        gameId: "0000001",

        sqlId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Once the page receives the response informs the user that the entry was created with success and send the new
information from the JSON included on the body of the response to the screen with the list of scheduled games so
it can be updated with the new entry.

The coach should then be able to see all its scheduled games plus the new entry as well as the options to remove
or edit an existent schedule and add new ones.

---------------------------------------------------
Test Failure - Create schedule returns unauthorized
---------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to add a new
schedule entry but its session ID is not valid to fulfill the requests.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
add a new entry by clicking on the create button.

Once the coach clicks the create button a new screen should appear with dropboxes filled with valid information,
the rest of the fields blank and a create button. An example of the fields on the create screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished filling the fields and clicks the create button it triggers a request to the backend in
order to create the entry.

Request:

* Method: **POST**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A *invalid* session id to be validated on the backend side
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **401 UNAUTHORIZED**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it informs the coach that its session is not valid so the operation couldn't
be completed.
For example: "Your session ID is not valid anymore, please refresh the page or login again."

---------------------------------------------------
Test Failure - Create a schedule with an empty body
---------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to add a new
schedule entry but the page sends the request without the JSON on the body.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
add a new entry by clicking on the create button.

Once the coach clicks the create button a new screen should appear with dropboxes filled with valid information,
the rest of the fields blank and a create button. An example of the fields on the create screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished filling the fields and clicks the create button it triggers a request to the backend in
order to create the entry.

Request:

* Method: **POST**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
* Body: **Empty**

Response:

* Status Code: **400 BAD REQUEST**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the user that the operation wasn't successful.
For example: Something happened and we weren't able to finish this operation.

The coach should then be given the option to try again, which will trigger the same request with the same
parameters again or go back to the creation page and change something else.

------------------------------------------------------
Test Failure - Create a schedule with an invalid value
------------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to add a new
schedule entry but the page sends the request with the JSON with invalid values in some fields.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
add a new entry by clicking on the create button.

Once the coach clicks the create button a new screen should appear with dropboxes filled with valid information,
the rest of the fields blank and a create button. An example of the fields on the create screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished filling the fields and clicks the create button it triggers a request to the backend in
order to create the entry.

Request:

* Method: **POST**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "INEXISTENT_OPPONENT_ID",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **400 BAD REQUEST**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the user that the operation wasn't successful.
For example: Something happened and we weren't able to finish this operation.

The coach should then be given the option to try again, which will trigger the same request with the same
parameters again or go back to the creation page and change something else.

----------------------------------------------------
Test Failure - Create a schedule with missing fields
----------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to add a new
schedule entry but the page sends the request with the JSON missing some fields.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
add a new entry by clicking on the create button.

Once the coach clicks the create button a new screen should appear with dropboxes filled with valid information,
the rest of the fields blank and a create button. An example of the fields on the create screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished filling the fields and clicks the create button it triggers a request to the backend in
order to create the entry.

Request:

* Method: **POST**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A valid session id to be validated on the backend side
* Body::

    Example of expected request JSON missing "opponentId" field:
    {
        gameId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **422 UNPROCESSABLE ENTITY**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the user that the operation wasn't successful.
For example: Something happened and we weren't able to finish this operation.

The coach should then be given the option to try again, which will trigger the same request with the same
parameters again or go back to the creation page and change something else.

----------------------------------------------------
Test Failure - Create schedule with unexpected error
----------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to add a new
schedule entry but the backend has trouble processing the request and returns an unexpected error.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be able to
add a new entry by clicking on the create button.

Once the coach clicks the create button a new screen should appear with dropboxes filled with valid information,
the rest of the fields blank and a create button. An example of the fields on the create screen could be:

* Date of the game (A calendar or a dropbox to select or type the date of the game)
* Opponent (A dropbox to pick an opponent that's registered on the database)
* Is the game at home? (A check box to inform if the game is at home)
* Type of the game (A dropbox to select which is the type of the game)
* Categories (A list of checkboxes to pick one or more of the categories registered on the database)

When the coach is finished filling the fields and clicks the create button it triggers a request to the backend in
order to create the entry.

Request:

* Method: **POST**
* Endpoint: https://www.hudlapi.com/coachID/schedules
* Parameters
    1. **coachID** - A valid coachID on the database
* Headers
    1. **session-id** - A *invalid* session id to be validated on the backend side
* Body::

    Example of expected request JSON:
    {
        gameId: "0000001",

        date: "2021-01-01T15:00:00",

        opponent: "Opponent1",

        opponentId: "000001",

        isHome: true,

        gameType: 0,

        categories: [ ]
    }

Response:

* Status Code: **500 INTERNAL SERVER ERROR**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the coach that something went wrong whilst trying to create the entry.
For example: Something went wrong on our side please try again.

The coach should then be able to see a retry button that will trigger the same request with the same parameters
again.

--------------------------------
Test Success - Delete a schedule
--------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to delete one or
multiple of its scheduled games.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be
able to delete one or more of the existent entries by clicking on the delete button.

Once the coach clicks the delete button a message is displayed to the coach asking for confirmation to proceed
with the deletion of the entry.

If the coach cancels the operation, nothing else happens and the message is dismissed.

If the coach confirms the operation it triggers a DELETE request to the backend in order to delete the entry.

Request:

* Method: **DELETE**
* Endpoint: https://www.hudlapi.com/coachID/schedules/gameID
* Parameters
    1. **coachID** - A valid coachID on the database
    2. **gameID** - A valid gameID for the given coachID
* Headers
    1. **session-id** - A valid session id to be validated on the backend side

Response:

* Status Code: **204 NO CONTENT**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response informs the user that the entry was deleted with success and also update the
screen with the list of scheduled games by removing the deleted entry.

The coach should then be able to see all its scheduled games minus the deleted entry as well as the options to
remove or edit an existent schedule and add new ones.

---------------------------------------------------
Test Failure - Delete schedule returns unauthorized
---------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to delete one or
multiple of its scheduled games but its session ID is not valid to fulfill the requests.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be
able to delete one or more of the existent entries by clicking on the delete button.

Once the coach clicks the delete button a message is displayed to the coach asking for confirmation to proceed
with the deletion of the entry.

If the coach cancels the operation, nothing else happens and the message is dismissed.

If the coach confirms the operation it triggers a request to the backend in order to delete the entry.

Request:

* Method: **DELETE**
* Endpoint: https://www.hudlapi.com/coachID/schedules/gameID
* Parameters
    1. **coachID** - A valid coachID on the database
    2. **gameID** - A valid gameID for the given coachID
* Headers
    1. **session-id** - An *invalid* session id to be validated on the backend side

Response:

* Status Code: **401 UNAUTHORIZED**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it informs the coach that its session is not valid so the operation couldn't
be completed.
For example: "Your session ID is not valid anymore, please refresh the page or login again."

------------------------------------------------
Test Failure - Delete schedule returns not found
------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to delete one or
multiple of its scheduled games but the entry doesn't exist on the database.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be
able to delete one or more of the existent entries by clicking on the delete button.

Once the coach clicks the delete button a message is displayed to the coach asking for confirmation to proceed
with the deletion of the entry.

If the coach cancels the operation, nothing else happens and the message is dismissed.

If the coach confirms the operation it triggers a request to the backend in order to delete the entry.

Request:

* Method: **DELETE**
* Endpoint: https://www.hudlapi.com/coachID/schedules/gameID
* Parameters
    1. **coachID** - A valid coachID on the database
    2. **gameID** - A *invalid* gameID for the given coachID
* Headers
    1. **session-id** - An valid session id to be validated on the backend side

Response:

* Status Code: **404 NOT FOUND**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response informs the user that the entry wasn't found on the database and also updates
the screen with the list of scheduled games by removing the respective entry.
For example: "The entry you tried to delete wasn't found on the database, it could be already deleted or it doesn't exist."

The coach should then be able to see all its scheduled games minus the deleted entry as well as the options to
remove or edit an existent schedule and add new ones.

----------------------------------------------------
Test Failure - Delete schedule with unexpected error
----------------------------------------------------

Tests the schedule functionality When the coach accesses https://www.hudl.com/schedule and wants to delete one or
multiple of its scheduled games but the backend has trouble processing the request and returns an unexpected error.

When the coach accesses https://www.hudl.com/schedule, after getting the list of its scheduled games it should be
able to delete one or more of the existent entries by clicking on the delete button.

Once the coach clicks the delete button a message is displayed to the coach asking for confirmation to proceed
with the deletion of the entry.

If the coach cancels the operation, nothing else happens and the message is dismissed.

If the coach confirms the operation it triggers a request to the backend in order to delete the entry.

Request:

* Method: **DELETE**
* Endpoint: https://www.hudlapi.com/coachID/schedules/gameID
* Parameters
    1. **coachID** - A valid coachID on the database
    2. **gameID** - A valid gameID for the given coachID
* Headers
    1. **session-id** - An *invalid* session id to be validated on the backend side

Response:

* Status Code: **500 INTERNAL SERVER ERROR**
* Headers
    1. **session-id** - The validated session id
* Body: **Empty**

Once the page receives the response it should inform the coach that something went wrong whilst trying to delete the entry.
For example: Something went wrong on our side please try again.

The coach should then be able to see a retry button that will trigger the same request with the same parameters
again.
