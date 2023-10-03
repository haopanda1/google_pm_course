# Databricks notebook source
# MAGIC %md 
# MAGIC
# MAGIC ### Agile Project Management

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Intro to Agile 

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Agile History
# MAGIC - `Waterfall Method` is the sequantial order execution of a project
# MAGIC - Project takes `agile` approach use iterative method (project process is repetitive over project life circle)
# MAGIC - Agile showed up when software industry is booming, so company need a new dev process so that `customer needs and wants can be met`
# MAGIC
# MAGIC ##### Agile vs Waterfall 
# MAGIC - `Waterfall` aims to create predicability and aviod changes, `agile` accepts customer needs and project scope is constantly changing. 
# MAGIC - `Agile` aims to get feedback from customer more quickly to make sure customer gets what they want
# MAGIC - **The core of agile is to reduce the waste such as not needed documents or not working on a feature customer will not use**
# MAGIC   - `Requirement`: items 100% needed to ensure project finishes
# MAGIC   - Team need work with stakeholders to prioritize urgent features
# MAGIC   - **documents in agile only provides need to know base**
# MAGIC - Agile has more frequent deliverable release; and waterfall has one big release at the end of project
# MAGIC - ![agile vs waterfall](https://cdn.slingshotapp.io/wp-content/uploads/2021/08/Scrum-vs-Waterfall-comparison-table.png)
# MAGIC
# MAGIC ##### Agile Menifesto
# MAGIC - ![agile](https://agileux.se/wp-content/uploads/2021/11/AgileManifesto-1030x850.png)
# MAGIC
# MAGIC ##### 12 Principles of Agile
# MAGIC - Value Delivery
# MAGIC   - How agile team delivers values
# MAGIC - Business Collaberation
# MAGIC   - How agile team colabs with stakeholders to add values
# MAGIC - Team Dynamic and Culture
# MAGIC   - How agile team creates right interpersonal dynamic for team
# MAGIC - Retrospect and Continouos Learning
# MAGIC   - How to continouosly increase project performance
# MAGIC
# MAGIC ##### VUCA in Agile Environment
# MAGIC - Volitility, Uncertainty, Complexity, and Ambiguity
# MAGIC - Agile is suitable when a project is VUCA

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### SCRUM 101

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Agile vs SCRUM
# MAGIC - agile a pholosophy and a mindset while SCRUM is a framework to materialize agile. 
# MAGIC
# MAGIC ##### Three Pillars of SCRUM 
# MAGIC - SCRUM works in iterations / timebox. 
# MAGIC - SCRUM works are divided into small chunks that build on each other
# MAGIC - Pillars 
# MAGIC   - Transparency
# MAGIC     - make the most significant aspect of our work visible to stakeholders
# MAGIC   - Inspection 
# MAGIC     - Conducting timely check toward outcome of sprint goal to verify project is on-track
# MAGIC   - Adaptation 
# MAGIC     - Learn from past mistakes and never repeat them
# MAGIC
# MAGIC ##### Five Values of SCRUM 
# MAGIC - Commitment: personally commit to achieve the goal of SCRUM team 
# MAGIC - Courage: Team member needs to have courage to do the right things 
# MAGIC - Focus: Everyone focus on the goal of SCRUM
# MAGIC - Openess: open on challenge and works
# MAGIC - Respect: Respect opinion of teammate
# MAGIC
# MAGIC ##### Roles in SCRUM 
# MAGIC - Product Owner: Build the right thing 
# MAGIC   - Help team understand what is needed & why it is important
# MAGIC   - Voice of Stakeholders
# MAGIC   - Stakeholder Focus / Decisive / Communication skills
# MAGIC - Dev Team: How team will deliver the product
# MAGIC - SCRUM Master: When a team will deliver a value; similar to PM
# MAGIC - [Great SCRUM Team](https://www.infoq.com/articles/great-scrum-team/)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### SCRUM Detial

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Product Backlog
# MAGIC - `Living Artifact`: items constantly add / remove from backlog
# MAGIC - Owned and adjusted by product owner
# MAGIC - **Prioritieze list of features**
# MAGIC - Guide and roadmap of your product
# MAGIC - Important Features 
# MAGIC   - Description of items
# MAGIC   - Business Value of Items 
# MAGIC   - Priority of an item
# MAGIC   - Estimated Effort of an item 
# MAGIC
# MAGIC ##### User Stories
# MAGIC - Short, simple description of a feature from perspective of a user
# MAGIC - Rule of INVEST
# MAGIC   - Independent: each user story is independent
# MAGIC   - Negotiable: 
# MAGIC   - Valuable:
# MAGIC   - Estimateble
# MAGIC   - Small
# MAGIC   - Testable
# MAGIC - Include following Items 
# MAGIC   - User Personna if applicable 
# MAGIC   - Defination of done 
# MAGIC   - Feedbacks 
# MAGIC - Acceptance Critiria: 
# MAGIC   - Checklist to determine whether a user story is done or not
# MAGIC
# MAGIC ##### Epic 
# MAGIC - A group or collection of user story
# MAGIC
# MAGIC ##### Backlog Refinement
# MAGIC - Objective for Backlog Refinement
# MAGIC   - ensure all items in backlog is up to date
# MAGIC   - ensure backlog is prioritize by product owner
# MAGIC   - item at the top of backlog is ready to deliver with clear acceptance critiria
# MAGIC
# MAGIC ##### Relative Estimation
# MAGIC - Instead of estimate absolute time and effort for a task, we use task A and compare with task B to get `relative effort`
# MAGIC - T Shirt Sizing 
# MAGIC - Story Points 
# MAGIC   - The reason we use fibonacchi number is because as story point gets higher, the uncertainty also get higher

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Sprint Planning
# MAGIC - The entire SCRUM team comes together, meet and confirm how much capacity are avaliable during the sprint
# MAGIC - **the end result is SCRUM backlog & Definition of Done**
# MAGIC
# MAGIC ##### Daily Standup and Review
# MAGIC - Standup is 15 mins event that answers 'what is done yesterday', 'what will be done today', and 'are there any road barrier'
# MAGIC - Review is insepct & close backlog. 
# MAGIC
# MAGIC ##### Product Increment vs MVP 
# MAGIC - Product after each sprint that considers releasable
# MAGIC - `Product Increment` is each feature that complete in a sprint, while `MVP` is a product / solution might take multiple sprint to develop but contain the full scale of a product that is ready to demo to a customer. 

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Velocity and Burndown Chart

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Velocity and Burndown Chart
# MAGIC - Burndown Chart: 
# MAGIC   - Measure time against the amount of work done (`user story`) and amount of work remaining
# MAGIC   - `Velocity`: how many points a team burns down during a single sprint
# MAGIC     - by understanding velocity, you can answer the following questions
# MAGIC     - 1: How long it will take to complete the entire product backlog 
# MAGIC     - 2: How much of your backlog will be completed by a particular time
# MAGIC   - `Velocity` should be stable once the team get used to work with each other. 
# MAGIC
# MAGIC ##### Velocity Do and Don't
# MAGIC - Do 
# MAGIC   - Becareful when sharing velocity with external stakeholders
# MAGIC   - Proceed with causion when using velocity as metric
# MAGIC - Don't 
# MAGIC   - Don't use velocity as performance metric 
# MAGIC   - Don't use velocity as comparision metric 
# MAGIC
# MAGIC ##### Agile Product Ownership 
# MAGIC - [LINK](https://www.youtube.com/watch?v=502ILHjX9EE)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Apply Agile in a Organization

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Maximize Value Driven Delivery
# MAGIC - Build the right thing
# MAGIC   - understand what they want and what is their goal
# MAGIC - Build the thing right
# MAGIC   - build only the requested feature
# MAGIC - Build it fast
# MAGIC   - you team know how user will interact with the tool

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Value Roadmap
# MAGIC - A agile way of mapping out the product dev process 
# MAGIC - Can demonstrate
# MAGIC   - where to go 
# MAGIC   - how to get there
# MAGIC   - what to accomplish
# MAGIC - Helps the team to explain the vision of product
# MAGIC - Identify important milestones
# MAGIC - Components
# MAGIC   - Product Vision
# MAGIC   - Product Roadmap 
# MAGIC   - Release Plan
# MAGIC     - SCRUM Master and Project Manager should always review the release plan before sprint planning
# MAGIC     - It needs related to team's capacity and velocity

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Scrum Master Role
# MAGIC - Design the play with the team 
# MAGIC   - how team works day to day
# MAGIC   - how team conduct sprint planning, review, and retro
# MAGIC   - how team can be better & celerbrate with team
# MAGIC - Provide feedback to the team
# MAGIC - Celeberate and learn with the team

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Sign of Team Dynamics and Culture Issues
# MAGIC - Low team morale
# MAGIC - lot of conflict & issue not get resolved
# MAGIC - Low Conflict

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Agile Team Challenge
# MAGIC - Value Delivery Challenge
# MAGIC   - Symptom
# MAGIC     - Missing expected delivery date
# MAGIC     - Members bruned out
# MAGIC     - Too many items in progress
# MAGIC   - Solution
# MAGIC     - more demo of the solution 
# MAGIC     - use retro
# MAGIC     - make sure that everyone understands what done means
# MAGIC     - Focus on only a few user stories per sprint
# MAGIC - Business Collaboration Issue
# MAGIC   - Symptom 
# MAGIC     - team is overwhelmed with critical feedback or change requests 
# MAGIC     - Us vs them mentality between dev and management
# MAGIC   - Solution
# MAGIC     - Do more demo 
# MAGIC     - Ensure changes to backlog only happens between sprints
# MAGIC - Team Dynamics and Culture Issues
# MAGIC   - Symptom 
# MAGIC     - Low team morale
# MAGIC     - lot of conflict & issue not get resolved
# MAGIC     - Low Conflict

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Common Agile Coaching Challenge
# MAGIC - Manage stable product roadmap 
# MAGIC   - Product ambition
# MAGIC     - product leadership is overly ambitious about what team can deliver
# MAGIC     - Solution
# MAGIC       - agree upfront how to handle new oppurtunities
# MAGIC       - set up regular roadmap reviews with entire team
# MAGIC   - Product Assumption 
# MAGIC     - team makes to many assuptions about project, which can jeopardize team's success
# MAGIC     - Solution
# MAGIC       - Document the assuption and make them transparent
# MAGIC       - Unbias user research
# MAGIC - Incomeplete implementation of SCRUM
# MAGIC   - only part of the SCRUM process being implemented (mix roles, skip events, etc)
# MAGIC - Experiencing lack of stability within team
# MAGIC   - Have a quick onboarding process 
# MAGIC   - Pair programming
# MAGIC   - Have shorter sprint

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Evolution of Agile
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Agile & DevOps
# MAGIC - [Link](https://www.cmswire.com/information-management/agile-vs-devops-whats-the-difference/)
