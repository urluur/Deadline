
# Deadline

Instructions from [UPM](https://putka-upm.acm.si/tasks/t/rok/en/):


>Deadlines for submitting homework assignments should not be missed. Unless explicitly permitted. The professor gave to the students in his course N tasks that they must submit by the given deadlines. He figured out that this requires a substantial amount of work. But instead of reducing the amount of work, he adjusted the scoring. Thus, it is not necessary to submit all tasks by their respective deadlines, but the number of points received for the task depends on the time of submission.
>
>Among the given N tasks, the i-th requires xi minutes to solve, and the deadline for its submission is ri. Times are measured in minutes from the beginning of the semester. If you submit the i-th task at the time ti, you will receive ri - ti points for it. So, if you submit the assignment early, you will receive positive points. If you miss the submission deadline, you will receive negative points for it. The total points for homework in the course are equal to the sum of the points for all assignments.
>
>Write a program that will calculate the maximum possible number of homework points you can score in the course. You must complete all the assignments.

## Input data:
The first line contains the number of tasks N, which are specified in the following lines. Each task is described by space-separated integers ri and xi.

### Input limits:
- 1 <= N <= 1000
- 1 <= ri, xi <= 1000

## Output data:
Output the maximum possible number of points for this course.

### Example input 1:


```
1
3 10
```

### Example output 1:
```
-7
```

### Example input 2:
```
10
83 12
66 9
64 1
26 10
35 15
12 3
51 12
64 3
5 14
9 4
```

### Example output 2:
```
95
```

## Solution

Soulution checked by UPM Judge 

![Putka](https://putka-upm.acm.si/static/img/logo/putka.a32410c73e30.png)
