# Cornwall Conservation Events
This is a simple web application that displays a list of conservation events in Cornwall. The events are stored in a database and can be added, edited and deleted. Site users can also comment on events.

Live link: [Cornwall Conservation Events](https://cornwall-conservation-events.herokuapp.com/)

## Table of Contents
1. [User Experience](#user-experience)
    1. [User Stories](#user-stories)
    2. [Wireframes](#wireframes)
    3. [How AI Was Used](#how-ai-was-used)
2. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Features left to Implement](#features-left-to-implement)    
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
    1. [Code Validation](#code-validation)
    2. [Lighthouse Testing](#lighthouse-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Acknowledgements](#acknowledgements)

## User Experience
### User Stories

1. As a site user I can click on an event so that I can read the full text

    **Acceptance criteria**
    - When an event post title is clicked on a detailed view of the event is seen.

2. As a site user I can view a paginated list of events so that I can select which event I want to view

    **Acceptance criteria**
    - Given more than one event in the database, these multiple events are listed.
    - When a user opens the main page a list of events is seen.
    - Then the user sees all event titles with pagination to choose what to read.

3. As a Site User / Admin I can view comments on an individual post so that I can read the conversation

    **Acceptance criteria**
    - Given one or more user comments the admin can view them.
    - Then a site user can click on the comment thread to read the conversation.

4. As a site user I can modify or delete my comment on a post so that I can be involved in the conversation

    **Acceptance criteria**
    - Given a logged in user, they can modify their comment
    - Given a logged in user, they can delete their comment

5. As a site admin I can approve or disapprove comments so that I can filter out objectionable comments

    **Acceptance criteria**
    - Given a logged in user, they can approve a comment
    - Given a logged in user, they can disapprove a comment

6. As a site user I can register an account so that I can comment on a post.

    **Acceptance criteria**
    - Given an email a user can register an account.
    - Then the user can log in.
    - When the user is logged in they can comment.

7. As a site admin I can create draft events so that I can finish writing the content later

    **Acceptance criteria**
    - Given a logged in user, they can save a draft event post
    - Then they can finish the content at a later time

8. As a site admin I can create, read, update and delete posts so that I can manage my event content

    **Acceptance criteria**
    - Given a logged in user, they can create an event
    - Given a logged in user, they can read an event post
    - Given a logged in user, they can update an event
    - Given a logged in user, they can delete an event

9. As a site user I can search for an event using tags so that I can find the event I am looking for

    **Acceptance criteria**
    - Given a search bar, a user can type in a tag
    - Then the user can see a list of events with that tag

### Wireframes

##Home Page
![Home Page](Static\images\home-page.png)

##Event Page
![Event Page](Static\images\event-page.png)

##About Page
![About Page](Static\images\about-page.png)

##Contact Page
![Contact Page](Static\images\contact-page.png)
