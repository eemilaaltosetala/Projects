-- AS OF 31.1.2022      data source: https://ourworldindata.org/coronavirus

SELECT *
FROM COVIDDEATHS
WHERE CONTINENT IS NOT NULL
ORDER BY 3,4

--SELECT * 
--FROM COVIDVACCINATIONS
--ORDER BY 3,4

--SELECT RELEVANT DATA

SELECT LOCATION, DATE, TOTAL_CASES, NEW_CASES, TOTAL_DEATHS, POPULATION
FROM COVIDDEATHS
ORDER BY 1,2


-- TOTAL CASES VS TOTAL DEATHS
-- CHANCE % OF DYING IF POSITIVE
SELECT LOCATION, DATE, TOTAL_CASES, TOTAL_DEATHS, (TOTAL_DEATHS/TOTAL_CASES)*100 AS DEATHS_PER_CASES
FROM COVIDDEATHS
WHERE LOCATION = 'FINLAND'
ORDER BY 1,2


-- TOTAL CASES IN POPULATION
-- % OF POPULATION THAT HAVE BEEN DIAGNOSED
-- FINLAND 8,8%
SELECT LOCATION, DATE, TOTAL_CASES, POPULATION, (TOTAL_CASES/POPULATION)*100 AS CASES_PER_POPULATION
FROM COVIDDEATHS
WHERE LOCATION = 'FINLAND'
ORDER BY 1,2


-- COUNTRIES WITH HIGHEST CASES PER POPULATION %
-- 46% OF ANDORRA HAS HAD COVID
SELECT LOCATION, POPULATION, MAX(TOTAL_CASES) AS INFECTIONRATE, MAX((TOTAL_CASES/POPULATION))*100 AS INFECTED_POPULATION_PERCENTAGE
FROM COVIDDEATHS
GROUP BY LOCATION, POPULATION
ORDER BY INFECTED_POPULATION_PERCENTAGE DESC



-- HIGHEST DEATHS BY CONTINENT
SELECT CONTINENT, MAX(CAST(TOTAL_DEATHS AS INT)) AS DEATH_COUNT
FROM COVIDDEATHS
WHERE CONTINENT IS NOT NULL
GROUP BY CONTINENT
ORDER BY DEATH_COUNT DESC



-- GLOBAL DEATHS PER CASES PERCENTAGE
SELECT SUM(NEW_CASES) AS CASES, SUM(CAST(NEW_DEATHS AS INT)) AS DEATHS, SUM(CAST(NEW_DEATHS AS INT))/SUM(NEW_CASES)*100 AS DEATHPERCENTAGE
FROM COVIDDEATHS
WHERE CONTINENT IS NOT NULL
ORDER BY 1,2


--HIGHEST CASES PER DAY IN FINLAND

SELECT MAX(NEW_CASES) AS MOST_CASES_PER_DAY, LOCATION
FROM COVIDDEATHS
WHERE LOCATION = 'FINLAND'
GROUP BY LOCATION
--THE DATE
SELECT DATE
FROM COVIDDEATHS
WHERE NEW_CASES = 14439


-- GLOBAL VACCINATIONS PER POPULATION
SELECT D.CONTINENT, D.LOCATION, D.DATE, D.POPULATION, V.NEW_VACCINATIONS,
SUM(CAST(V.NEW_VACCINATIONS AS FLOAT)) OVER (PARTITION BY D.LOCATION
ORDER BY D.LOCATION, D.DATE) AS TOTAL_PEOPLE_VACCINATED
FROM COVIDDEATHS D
JOIN COVIDVACCINATIONS V
ON D.LOCATION = V.LOCATION
AND D.DATE = V.DATE
WHERE D.CONTINENT IS NOT NULL
ORDER BY 2,3


--PPL VACCINATED BY COUNTRY

SELECT D.CONTINENT, D.LOCATION, D.DATE, D.POPULATION
, MAX(V.TOTAL_VACCINATIONS) AS ROLLINGPEOPLEVACCINATED
--, (ROLLINGPEOPLEVACCINATED/POPULATION)*100
FROM COVIDDEATHS D
JOIN COVIDVACCINATIONS V
	ON D.LOCATION = V.LOCATION
	AND D.DATE = V.DATE
WHERE D.CONTINENT IS NOT NULL 
GROUP BY D.CONTINENT, D.LOCATION, D.DATE, D.POPULATION
ORDER BY 1,2,3


--CTE PERCENTAGE_OF_PEOPLE_VACCINATED
WITH POPULATION_VS_VACCINATION (CONTINENT, LOCATION, DATE, POPULATION, NEW_VACCINATIONS, TOTAL_PEOPLE_VACCINATED)
AS

(
SELECT D.CONTINENT, D.LOCATION, D.DATE, D.POPULATION, V.NEW_VACCINATIONS,
SUM(CAST(V.NEW_VACCINATIONS AS FLOAT)) OVER (PARTITION BY D.LOCATION
ORDER BY D.LOCATION, D.DATE) AS TOTAL_PEOPLE_VACCINATED
FROM COVIDDEATHS D
JOIN COVIDVACCINATIONS V
ON D.LOCATION = V.LOCATION
AND D.DATE = V.DATE
WHERE D.CONTINENT IS NOT NULL
--ORDER BY 2,3
)
SELECT *, (TOTAL_PEOPLE_VACCINATED/POPULATION)*100 AS PERCENTAGE_OF_PEOPLE_VACCINATED
FROM 
POPULATION_VS_VACCINATION



-- WITH TEMP

DROP TABLE IF EXISTS #PERCENTAGEVACCINATED
CREATE TABLE #PERCENTAGEVACCINATED
(
CONTINENT NVARCHAR(255),
LOCATION NVARCHAR(255),
DATE DATETIME,
POPULATION NUMERIC,
NEW_VACCINATIONS NUMERIC,
TOTAL_PEOPLE_VACCINATED NUMERIC
)


INSERT INTO #PERCENTAGEVACCINATED
SELECT D.CONTINENT, D.LOCATION, D.DATE, D.POPULATION, V.NEW_VACCINATIONS,
SUM(CAST(V.NEW_VACCINATIONS AS FLOAT)) OVER (PARTITION BY D.LOCATION
ORDER BY D.LOCATION, D.DATE) AS TOTAL_PEOPLE_VACCINATED
FROM COVIDDEATHS D
JOIN COVIDVACCINATIONS V
ON D.LOCATION = V.LOCATION
AND D.DATE = V.DATE
--WHERE D.CONTINENT IS NOT NULL
--ORDER BY 2,3

SELECT *, (TOTAL_PEOPLE_VACCINATED/POPULATION)*100 AS PERCENTAGE_OF_PEOPLE_VACCINATED
FROM #PERCENTAGEVACCINATED



--VIEW(S) FOR VISUALIZATIONS 

CREATE VIEW 
PERCENTAGEVACCINATED AS 
SELECT D.CONTINENT, D.LOCATION, D.DATE, D.POPULATION, V.NEW_VACCINATIONS,
SUM(CAST(V.NEW_VACCINATIONS AS FLOAT)) OVER (PARTITION BY D.LOCATION
ORDER BY D.LOCATION, D.DATE) AS TOTAL_PEOPLE_VACCINATED
FROM COVIDDEATHS D
JOIN COVIDVACCINATIONS V
ON D.LOCATION = V.LOCATION
AND D.DATE = V.DATE
WHERE D.CONTINENT IS NOT NULL










