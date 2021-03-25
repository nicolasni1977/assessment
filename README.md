# devops
1.	Introduction of Assessment
The company has setup an on-premises BitBucket server to use as the company-wide source code repository. Multiple development teams are using this BitBucket server. Each development team can have multiple projects and multiple repositories in each project. The project manager of the development team is designated as the admin for each project.
Some of the issues faced include and not limited to:
•	Repository being public in BitBucket when it should not be
•	Developer still having access to old repositories after rotating to another team

As part of the central DevOps team, you have been tasked to write a script that will help a project admin assess if the permissions of their projects and repositories have been configured correctly.

The script must take in Inputs:
•	Username and password of project admin
•	Team members and roles
And must provide Output:
•	List of project and repositories with permissions that may not have been configured correctly


2.	Thought Process
As BitBucket can be a brand-new tool for someone like me. To understand it better and easier, I use analogy to assist on understanding using familiar Windows Operating System. 

My thought is like these: 
(Left side BitBucket Constructs < can be think as > Right side Windows Operation System Constructs)
	BitBucket Server System < can be think as > Windows Operation System
	BitBucket Project < can be think as > Windows OS File Parent Directory for Folders
	BitBucket Repository < can be think as > Windows OS Folder
	BitBucket User < can be think as > Windows OS User
	BitBucket Group < can be think as > Windows OS Group
	BitBucket Global Permission < can be think as> Windows OS User Account Control Setting
	BitBucket Project Permission < can be think as > Windows OS Parent Directory Permission
	BitBucket Repository Permission < can be think as > Windows OS Folder Permission
	BitBucket System Admin < can be think as > Windows OS administrator group
	BitBucket Project Admin Role < can be think as > Windows OS Directory Full Control Permission
	BitBucket Repository Admin Role < can be think as > Windows OS Folder Full Control Permission
	BitBucket Read/Write Permission < can be think as > Windows OS Directory/Folder Read/Write Permission
	BitBucket Public Access for Project < can be think as > Windows OS Share with Everyone for Directory
	BitBucket Public Access for Repository < can be think as > Windows OS Share with Everyone for Folder

With above analogy and mapping in mind, if I can write a script to enumerate Windows OS specific parent directory path (think of BitBucket Project), underneath the path what are the folders (think of BitBucket Repository) and their permissions settings, then I can generate a report to look at the wrong permission settings of parent directory (project) and repositories (folders). Use the same logic, just change script syntax to adapt to BitBucket API, I get the solution!

I decide to use Pseudocode test present logic behind as currently I am not proficient in scripting language (I could copy script from Internet and change it a bit, but that is not mine and not what I would like to do:)
