-- Databricks notebook source
-- MAGIC %md 
-- MAGIC
-- MAGIC ### Project Planning

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Before Project Planning Phase

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC - Project manager got assigned
-- MAGIC - Project goal, scope, and deliverable have to be approved
-- MAGIC - Team member got assigned
-- MAGIC - Stakeholder assigned project charter

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Important Items in Planning

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC - Timeline: Start date, end date, and milestone date
-- MAGIC - Budget: Total cost of completing a project
-- MAGIC - Risks: Searching for potential problems and find out solution to mitigate them

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Project Kickoff Meeting

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC - it is the first meeting that all team members come together to understand the scope of project and make sure everyone has the same vision; also understand roles. 
-- MAGIC - `Who are invited`: 
-- MAGIC   - All member from RACI chart
-- MAGIC   - Project sponsors 
-- MAGIC   - stakeholders
-- MAGIC - Content of meeting
-- MAGIC   - Introduction
-- MAGIC   - Background of project
-- MAGIC     - How project came to be
-- MAGIC     - Why project matter
-- MAGIC   - Goal and scope (boundary of project)
-- MAGIC - Role
-- MAGIC - Collaboration
-- MAGIC   - Shared project and documentation (which tool the team will use)
-- MAGIC   - Communication expectation (how team communicate with each other, frequency of communication, etc)

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Project Milestone and Tasks

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC - Project Milestone is the important event / deliverable of a project, milestone has to complete ontime
-- MAGIC - Project tasks is a task that has a deadline
-- MAGIC - Why Project Milestone Important
-- MAGIC   - Clear understand of project requriement
-- MAGIC   - Force you breakdown project into chunks
-- MAGIC   - Help your project on track
-- MAGIC   - Serve as highlight point to stakeholders

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### How to set Projet Milestone

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC - Evaluate your project as a whole
-- MAGIC   - refer back to project charter to remind you the goal and scope of project
-- MAGIC - List items the team needs to do to achieve goals
-- MAGIC   - those big items are milestone
-- MAGIC   - small items are tasks
-- MAGIC - Assign each milestone with a deadline
-- MAGIC   - follow up with team member to understand how long a milestone will take
-- MAGIC - `Pitfalls`  
-- MAGIC   - don't set too many milestones 
-- MAGIC   - don't treat tasks as milestone
-- MAGIC   - don't seperate milestone from tasks
-- MAGIC - `Work Break Down Structure - WBS`
-- MAGIC   - A tool that breakdown milestone and tasks into hierachy such as DevOps

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Project Plan

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Component of Project Plan
-- MAGIC - Task 
-- MAGIC - People
-- MAGIC - Milestone
-- MAGIC - Documentation
-- MAGIC   - Budget 
-- MAGIC   - Risk Management Plan
-- MAGIC - Time (start & End)
-- MAGIC
-- MAGIC ##### Project Plan vs Project Charter
-- MAGIC - Project charter is the output from project initialization phase
-- MAGIC - Project plan is the output from project planning stage
-- MAGIC - these two documents are complimentary
-- MAGIC - Project plan is low level opeartional documentation & project charter is high level strategic plan
-- MAGIC
-- MAGIC ##### Core of Project Planning
-- MAGIC - Project schedule
-- MAGIC - Scope and Goal
-- MAGIC   - Includes in project charter 
-- MAGIC - WBS / DevOps
-- MAGIC   - RACI charter (who is responsible for what)
-- MAGIC   - Breakdown project into milestone and tasks
-- MAGIC - Budget 
-- MAGIC   - it is heavily impacted by scope and tasks of a project 
-- MAGIC   - if you don't have automacy to determine budget, make sure check in with finance guy regularly
-- MAGIC - Management Plan
-- MAGIC   - Project change management plan
-- MAGIC   - Communication plan
-- MAGIC   - risk management plan
-- MAGIC
-- MAGIC ##### Time Estimation vs Difficulty Estimation 
-- MAGIC - Time estimation is the time required to complete a task
-- MAGIC - Effort estimation is the effort needed to complete a task
-- MAGIC
-- MAGIC ##### Time Estimation of Project Tasks
-- MAGIC - Active Time & Inactive Time 
-- MAGIC   - Like paining a wall, the active time (time to do the work) may be 30 mins but you need 20 hours inactive time (wait wall to dry) to achieve the task
-- MAGIC - `Consider sub tasks when planning estimation`
-- MAGIC -  `Use time buffer to include unforseenable delay`
-- MAGIC - **Task Buffer and Project Buffer**
-- MAGIC   - Task buffer should be used on tasks that is out of control of project team
-- MAGIC   - Project buffer put extra time on project as a whole

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Capacity Plan

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Critical Path
-- MAGIC - A list of project milestones you need to meeting project goal and schedule; as well as mandotory tasks that contribute to completion of a task
-- MAGIC - `It contains the bare minimum tasks you need to do to accomplish the goal`
-- MAGIC - You need identify which tasks / milestones can happen sequentially or in parallel
-- MAGIC - **identify project with a float (tasks have set amount of time before the whole project will be negatively impacted; these are high priority tasks)**
-- MAGIC - [How to Use Critical Path](https://www.workamajig.com/blog/critical-path-method)
-- MAGIC
-- MAGIC ##### Time Estimation with Teammate
-- MAGIC - Ask Open ended question
-- MAGIC - Practicing Empathy

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Project Budget

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Definition 
-- MAGIC - Resource needed to achive project goal and objective
-- MAGIC - It takes place to project initialization phase of your project planning & it can be adjusted though the life cycle of project
-- MAGIC - **Budgeting usually happens in conjouncation with scheduling process**
-- MAGIC
-- MAGIC ##### Forcast Budget
-- MAGIC - a cost estimation over a period of time & **it is based on project milestones**
-- MAGIC
-- MAGIC ##### Key Components
-- MAGIC - Understand stakeholders needs 
-- MAGIC - Account for surprising expenses
-- MAGIC - Maintaining Adaptbility
-- MAGIC - Review and reforecast thoughout the project
-- MAGIC
-- MAGIC ##### Types of Factors in Budgeting
-- MAGIC - `Resouce Cost Rate`: The cost to get job done
-- MAGIC - `contigency budget`: the extra money in case unforeseenable events happen
-- MAGIC - `Cost of Quality`: Cost to ensure the product quality is aligned with expectation
-- MAGIC - `Reserve Analysis`: review your project's milestone and find out any risks, then add contigency budget on top of it
-- MAGIC
-- MAGIC ##### Direct Cost & Indirect Cost
-- MAGIC - `Direct Cost`: These are costs for items that are necessary in order to complete your project
-- MAGIC - `Indirect Cost`: These are costs for items which do not directly lead to the completion of your project but are still essential for the project team to do their work. They are also referred to as overhead costs.
-- MAGIC
-- MAGIC ##### Baseline Cost
-- MAGIC - Cost that you start with at the begining of your project
-- MAGIC - It is useful to constantly refer to baseline budget and how your projection does 
-- MAGIC - You should re-establish basedline when needed

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Costs Payment Types 
-- MAGIC - Fixed Contract: Paid by achivement of milestone
-- MAGIC - Time and Material Contract: Paid monthly or weekly
-- MAGIC
-- MAGIC ##### Why Going Under Budget is not Good
-- MAGIC - it means you could have put in more money and have better quality of your project
-- MAGIC
-- MAGIC ##### Common Pitfalls of Budgeting
-- MAGIC - Budget Pre-Allocation 
-- MAGIC   - Budget already set before the project initialiezed
-- MAGIC   - this can happen in company with tighter budget control
-- MAGIC - Inaccurate TCO
-- MAGIC   - `TCO`: Total cost of ownership such as buy a car includes MSRP, dealer markup, license fee etc
-- MAGIC   - When calculate budget for a project it is important to consider costs such as maintainance cost
-- MAGIC - Scope Creep
-- MAGIC   - Might from unclear statement of work
-- MAGIC   - Unattainable timeframe and deadline 
-- MAGIC   - Last miniute ask from stakeholders

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Term Related to Budgeting
-- MAGIC - Cash Flow: 
-- MAGIC   - inflow and outflow of cash in your project
-- MAGIC   - monitor outflow ensure you have enough fund and visibility about a project
-- MAGIC - CAPEX 
-- MAGIC   - Capital Expenses
-- MAGIC   - organization's major, long-term, upfront expenses such as buildings, equipment, and vehicles
-- MAGIC - OPEX 
-- MAGIC   - Operational Expenses 
-- MAGIC   - Short term expenses that required for day to day tasks in running a company. 
-- MAGIC - Contingency Reserves
-- MAGIC   - money reserved for **planned** costs 
-- MAGIC   - this also refer `buffers`
-- MAGIC   - it usually represent in `dollor amount`
-- MAGIC - Management Reserves
-- MAGIC   - money reserved for **unplanned** costs 
-- MAGIC   - it usually represent as `percentage` of a project's total expense

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Procurement

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Vendor Management
-- MAGIC - Sourcing Vendors
-- MAGIC - Getting quotes for vendors' work 
-- MAGIC - choose vendor
-- MAGIC
-- MAGIC ##### Procurement Process 
-- MAGIC - Find out what additional resource you need to achive project goal
-- MAGIC - Select which vendor to use
-- MAGIC - Contract writing
-- MAGIC - Control
-- MAGIC - Completing
-- MAGIC
-- MAGIC ##### Types of Procurement
-- MAGIC - `Agile procurement management`
-- MAGIC   - collab from both project team and end supplier
-- MAGIC   - emphasis on relationship between these parties
-- MAGIC   - project team plays an important role on identifying what needs to be procured
-- MAGIC   - Living contract: contract can be negotiated multiple times
-- MAGIC - `Traditional procurement management`
-- MAGIC   - Focus on clear contracts with clear term and deliverables 
-- MAGIC   - Project manager, not team, responsible for end to end procurement
-- MAGIC   - Contract may feature lengthy and extensive docs
-- MAGIC
-- MAGIC ##### Procurement Documentations
-- MAGIC - NDA: Non Disclosure Agreement
-- MAGIC - RFP: Request for Proposal
-- MAGIC   - a document that outlines the details of the project
-- MAGIC - Statement of Work
-- MAGIC   - send to the selected vendor
-- MAGIC   - You should ask SME for tech related questions 

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC #### Risk Management

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Risk vs Issue
-- MAGIC - `Risk`: is something that could happen 
-- MAGIC - `Issue`: is a `materialized risk`, is a real problem that can affect the ability to finish work
-- MAGIC
-- MAGIC ##### Risk Management Benifits
-- MAGIC - Tells you what could go wrong
-- MAGIC - Who you need consult with 
-- MAGIC - How potential risk can be mitigated
-- MAGIC
-- MAGIC ##### Risk Management Phases
-- MAGIC - Identify Risk
-- MAGIC   - Identify and define risks in your project
-- MAGIC - Analyze risk
-- MAGIC   - Determine the likelihood of a risk to impact your project
-- MAGIC - Evaluate risk
-- MAGIC   - Determine which risks to prioritize
-- MAGIC - Treat risk
-- MAGIC   - Make a plan on how to treat risks
-- MAGIC - Monitor and control risk
-- MAGIC   - Assign team member to monitor the risk if needed
-- MAGIC
-- MAGIC ##### How to Find Out Risks - Brainstorming & Risk Assessment Session
-- MAGIC - Use `RACI` chart to determine who to invite
-- MAGIC - Create `Cause and Effect Diagram` which shows the possible causes of an event or risk
-- MAGIC - ![Cause and effect diagram / Fishbone Diagram](https://www.juran.com/wp-content/uploads/2019/05/Cause-Effect-Diagram_L-01.png)
-- MAGIC   - Identify the problem 
-- MAGIC   - Identify categories for risks
-- MAGIC   - Identify risks in each category
-- MAGIC - Once you finished `Cause and Effect Diagram`, list all risks into [Risk Register](https://www.wrike.com/blog/what-is-a-risk-register-project-management/)
-- MAGIC - To fill the `impact and possibility of occure` part, you need 
-- MAGIC   - `Impact`: the scale of impact if it were occure (high, medium, low)
-- MAGIC   - `Probability`: the likelyhood of a risk to occure
-- MAGIC   - ![probability and impact chart](https://cdn-cnhfh.nitrocdn.com/jsHsUxJJAapjeJICfnGvtaAAOHZlckTe/assets/static/optimized/rev-508d950/2022/08/24135641/Picture1.png)
-- MAGIC - How you team response to those risks is depends on your `risk appetite`
-- MAGIC
-- MAGIC ##### Type of Risks
-- MAGIC - `Time`: The possibility of a project can prolonged
-- MAGIC - `Budget`: Cost of project increases 
-- MAGIC - `Scope`: Project objectives cannot achieve
-- MAGIC - `External`: Risks you have no control over
-- MAGIC - **Single Point of Failure**: Risk that has catastrophic implication on project
-- MAGIC - `Dependency`
-- MAGIC
-- MAGIC ##### How to Deal with Single Point of Failure
-- MAGIC - Aviod
-- MAGIC   - Eliminate risk by choose a different plan
-- MAGIC - Transfer
-- MAGIC   - Send ths risk to other teams
-- MAGIC   - ie: instead of make your own chips, you buy it from other company
-- MAGIC - Mitigate 
-- MAGIC   - reduce the scope of impact of a risk by using both plans. ie: use two supplier instead of one. 
-- MAGIC - Accept 
-- MAGIC   - Not taking measure against risk and accept the risk as part of business cost (not recommended for single point of failure)
-- MAGIC   - Fit risks of low probability and impact
-- MAGIC
-- MAGIC ##### Types of Dependencies
-- MAGIC - Finish to Start
-- MAGIC   - Task A need to be finished before Task B can start
-- MAGIC
-- MAGIC - Finish to Finish
-- MAGIC   - Task A need to be finished before Task B can finish
-- MAGIC
-- MAGIC - Start to Start
-- MAGIC   - Task A need to be started before Task B can start
-- MAGIC
-- MAGIC - Start to Finish
-- MAGIC   - Task A need to be started before Task B can finish

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Create Effective Communication Plan

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC
-- MAGIC ##### Communication Plan 
-- MAGIC - Outlines process, expectation, and types of communication for a project
-- MAGIC - Items to Include
-- MAGIC   - What need to be communicated
-- MAGIC   - When communication needs to be happened
-- MAGIC   - Who need to communicate 
-- MAGIC   - Why and How to communicate 
-- MAGIC   - Where the information being stored
-- MAGIC
-- MAGIC ##### Form a Communication Plan 
-- MAGIC - Refer back to RACI chart to identify stakeholdersa and corresponding communication methods
-- MAGIC - Identify Topics
-- MAGIC   - Stakeholders 
-- MAGIC   - Method of Communicating 
-- MAGIC   - Frequency
-- MAGIC   - Key Date (optional)
-- MAGIC   - Delivery Method (Zoom, email, etc)
-- MAGIC   - Overoll Goal of Communication
-- MAGIC   - Who is the owner
-- MAGIC - ![Communication Plan](https://clickup.com/blog/wp-content/uploads/2022/12/Google-Sheets-Communication-Plan-Template-1400x599.png)
-- MAGIC - Ask Stakeholder about Communication Plan
-- MAGIC   - What is working 
-- MAGIC   - What is not working 
-- MAGIC   - Where improvement can be made
-- MAGIC
-- MAGIC ##### Only Share Information on Need to Know Bases 
