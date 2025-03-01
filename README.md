# Approach
My approach to using the SWAPI focuses on collecting data about the starships and pulling the pilots data. The output format is similar to a file structure with directories. Ships act as directories and output the pilots names beneath them.

# Assumptions
This is assuming that this is the desired scructure of output. If separate lists of pilots and starships was requested, pilots would have been aggregated into one list to pull the names after handling every starship.

# Steps 
(Assuming docker is installed and familiar with github)
1. Clone Repo
2. Build with Docker
 - docker build -t starship_image
3. Run
 - docker run --rm starship_image
4. View results on screen
   
# docker_example

To build use:
`docker build -t <image name> .`

To run use:
`docker run --rm <image name>`

# Conclusion and additional notes
- If there was a known size of data, we could measure the responses to ensure completeness and reattempt where necessary.

- To handle a man in the middle attack, we could verify data against other known sources.

- For further optimization we could pass off data handling to a seperate thread.

- Scaling data collection becomes more difficult as there are rate limiting features on SWAPI. If necessary, assuming SWAPI could handle the volume of requests, requesting data through multiple IP addresses could be done, though might be against terms of service so more research would need to be done to ensure compliance.

- 
