# Databricks notebook source
# MAGIC %md 
# MAGIC
# MAGIC ### Project Execution & Closing

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### The importance of Tracking a Project

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### The importance of Tracking a Project
# MAGIC - Tracking ensures transparency which is essential for decision making
# MAGIC - Ensures all stakeholders has visibility of milestones and goals
# MAGIC - Ensure team to recognize risks that can derail your project
# MAGIC
# MAGIC ##### Common Items to Track
# MAGIC - Project Schedule (tasks & Schedule)
# MAGIC - Status of action items
# MAGIC - Cost 
# MAGIC - Key decision, dependency, changes, and risk of a project (**especially scope change**)
# MAGIC
# MAGIC ##### Tracking Methods 
# MAGIC - Gannet Chart
# MAGIC   - Stay on top of schedule
# MAGIC   - Useful for project with many dependencies, tasks, activities, or milestones
# MAGIC   - Benifits
# MAGIC     - Help team stay on schedule
# MAGIC     - Project with lots of tasks 
# MAGIC     - Project with large team becuase ownership and responsibility are explicitly laid out
# MAGIC - Roadmap 
# MAGIC   - Track big milestones
# MAGIC   - It is for stakeholders
# MAGIC   - It is useful for: 
# MAGIC     - High level tracking of large milestone
# MAGIC     - Illustrate how project progress overtime
# MAGIC - Burnout Chart
# MAGIC   - Suit for tracking tasks
# MAGIC
# MAGIC ##### Project Status Report
# MAGIC - Project name: 
# MAGIC   - The project name should be specific to the purpose of the project so that the overall goal of the project can be understood at-a-glance. 
# MAGIC
# MAGIC - Date: 
# MAGIC   - You will create project status reports many times during the course of a project’s implementation phase. Reports can be created weekly or monthly—it all depends on the stakeholders’ need and pace of the project. Adding the date to each status report acts as a reference point for your audience and also creates a history log of the project’s status over time. 
# MAGIC
# MAGIC - Summary: 
# MAGIC   - The summary condenses the project’s goals, schedule, highlights, and lowlights in one central place for easy stakeholder visibility. Usually, the summary section will be followed by, or grouped with, the timeline summary and the overall project status.
# MAGIC
# MAGIC - Status: 
# MAGIC   - As you can imagine, status is a crucial piece. The status of the project illustrates your actual progress versus your planned progress. In project management, a common way to depict this is through RAG (red, amber, green), or Red-Yellow-Green, status reporting. RAG follows a traffic light pattern to indicate progress and status.
# MAGIC   - Red 
# MAGIC     - indicates that there are issues that need resolution and that the project may be delayed or go significantly over budget. 
# MAGIC   - Amber/Yellow 
# MAGIC     - means that there are potential issues with schedule or budget, but that the issues can likely be resolved with corrective actions. 
# MAGIC   - green 
# MAGIC     - means the schedule and budget are doing fine and that the project is on track. You can use RAG to indicate the overall project status, as well as milestone status. Every project team and stakeholder may have a slightly different perspective on what the colors mean and how urgent it is to escalate issues when they see an amber/yellow or red status, so it’s important to make sure everyone understands what the different color statuses mean for your project.
# MAGIC
# MAGIC - Milestones and tasks: 
# MAGIC   - A summary of the project’s major milestones thus far and current tasks helps the team and stakeholders easily visualize the progress of those elements. In a project plan, you will typically depict the tasks and milestones as ‘not started,’ ‘in progress’ or ‘completed’ at an item-by-item level. But, in the project status report, it is common to summarize these items into two categories to better communicate the status. You’ll use key accomplishments to detail what has happened, and upcoming to detail what big milestones you will accomplish next.
# MAGIC
# MAGIC - Issues: 
# MAGIC   - The issues include your project's current roadblocks and potential risks. Status reports are an important opportunity to set expectations with your stakeholders. If your project status is red or amber, you can flag what is preventing you from being where you planned to be. You can also use this opportunity to state your plan to get the project back to green, and ask for any resources or help you may need to do so. You will learn more about communicating big risks and issues in the upcoming videos.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Why Change and Risk Happens - Changes Impact Project
# MAGIC - Change of Dependency
# MAGIC - Change of Priority
# MAGIC - Capacity and People
# MAGIC - Limitation on budget or resource
# MAGIC - Scope Creep
# MAGIC - Force Majeure: Unforeseenable disaster and crisis
# MAGIC
# MAGIC ##### Why Change and Risk Happens - How to Request Changes
# MAGIC - Change of Requests Form

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Dependency - How to Track
# MAGIC - Completion of one task is related to completion of another tasks
# MAGIC - `Internal Dependency`: the relationship between two tasks within the same project
# MAGIC - `External Dependency`: the relationship between two tasks is outside of organization / project
# MAGIC - `Mandotory Dependency`: a task has to be perform legally before next one
# MAGIC - `Discretionary Dependencies`: Tasks that could occur on their own, but team chose to make them rely on one another
# MAGIC - `Dependency Management`: the process of managing interrelated tasks and resources to ensure the overall project is completed

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Risk Management
# MAGIC - It is a good idea to create a `risk register` when dealing with risk management
# MAGIC - You can create `Risk exposure` to measure potential future loss from an activities or events
# MAGIC   - It is the same concept as `possibility and impact chart`
# MAGIC - Use `ROAM Techniques` to manage risks
# MAGIC   - Resolved, Owned, Accepted, and Mitigated
# MAGIC   
# MAGIC ##### Risk Management - Escalation 
# MAGIC - Escalation standard should be established before the start of a project
# MAGIC - PM should escalate when the first sign of critical issue occurs
# MAGIC   - Budget
# MAGIC   - Time 
# MAGIC   - Scope
# MAGIC - `Trench War` and `Bad Compromise`
# MAGIC   - Trench war: occur when two peers or groups cannot come to an agreement
# MAGIC   - Bad Compromise: Two parties settle on a "solution" but end product still suffers
# MAGIC - Effective Escalation Email 
# MAGIC   - Maintain a Friendly Tone
# MAGIC   - State your connection to project
# MAGIC   - Explain the problem
# MAGIC   - Explain the consequence
# MAGIC   - Proposed actions 
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Quality Management & Continouos Improvement
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Quality Management Concepts
# MAGIC - Quality Standard
# MAGIC   - provide requirements, specifications, or guidelines
# MAGIC   - set at the beginning of your project
# MAGIC - Qualit Planning 
# MAGIC   - Action os project manager to establish a process for identify standard of quality
# MAGIC - Quality Assurance
# MAGIC   - is a review process that evaluates whether the project is moving toward delivering a high-quality service or product. 
# MAGIC - Quality Control
# MAGIC   - monitoring project results and delivery to determine if they are meeting desired results. 
# MAGIC   - **A subset of quality assurance activities, it is more related to inspection**
# MAGIC   - [Quality Control vs Quality Assurance](https://asq.org/quality-resources/quality-assurance-vs-control)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Customer Satisfiction 
# MAGIC - Pre-Launch Survey
# MAGIC - After-Launch Survey
# MAGIC - Beta Test / UAT Test
# MAGIC   - `Critical User Journey / Test Cases`: a series of action user can take to accomplish something
# MAGIC   - `Edge Cases`: rare outliers that hard to see in developement
# MAGIC   
