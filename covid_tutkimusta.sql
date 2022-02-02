-- as of 31.1.2022

select *
from CovidDeaths
where continent is not null
order by 3,4

--select * 
--from CovidVaccinations
--order by 3,4

--select relevant data

select location, date, total_cases, new_cases, total_deaths, population
from CovidDeaths
order by 1,2


-- total cases vs total deaths
-- chance % of dying if positive
select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as deaths_per_cases
from CovidDeaths
where location = 'Finland'
order by 1,2


-- total cases in population
-- % of population that have been diagnosed
-- Finland 8,8%
select location, date, total_cases, population, (total_cases/population)*100 as cases_per_population
from CovidDeaths
where location = 'Finland'
order by 1,2


-- countries with highest cases per population %
-- 46% of Andorra has had covid
select location, population, MAX(total_cases) as InfectionRate, max((total_cases/population))*100 as infected_population_percentage
from CovidDeaths
group by location, population
order by infected_population_percentage desc



-- highest deaths by continent
select continent, MAX(cast(total_deaths as int)) as death_count
from CovidDeaths
where continent is not null
group by continent
order by death_count desc



-- global deaths per cases percentage
select SUM(new_cases) as cases, SUM(cast(new_deaths as int)) as deaths, SUM(cast(new_deaths as int))/Sum(new_cases)*100 as DeathPercentage
from CovidDeaths
where continent is not null
order by 1,2


--highest cases per day in Finland

select MAX(new_cases) as most_cases_per_day, location
from CovidDeaths
where location = 'Finland'
group by location
--the date
select date
from CovidDeaths
where new_cases = 14439


-- global vaccinations per population
select d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(cast(v.new_vaccinations as float)) OVER (partition by d.location
order by d.location, d.date) as total_people_vaccinated
from CovidDeaths d
join CovidVaccinations v
on d.location = v.location
and d.date = v.date
where d.continent is not null
order by 2,3


--cte percentage_of_people_vaccinated
with population_vs_vaccination (continent, location, date, population, new_vaccinations, total_people_vaccinated)
as

(
select d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(cast(v.new_vaccinations as float)) OVER (partition by d.location
order by d.location, d.date) as total_people_vaccinated
from CovidDeaths d
join CovidVaccinations v
on d.location = v.location
and d.date = v.date
where d.continent is not null
--order by 2,3
)
select *, (total_people_vaccinated/population)*100 as percentage_of_people_vaccinated
from 
population_vs_vaccination



-- with temp

drop table if exists #PercentageVaccinated
create table #PercentageVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
total_people_vaccinated numeric
)


insert into #PercentageVaccinated
select d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(cast(v.new_vaccinations as float)) OVER (partition by d.location
order by d.location, d.date) as total_people_vaccinated
from CovidDeaths d
join CovidVaccinations v
on d.location = v.location
and d.date = v.date
--where d.continent is not null
--order by 2,3

select *, (total_people_vaccinated/population)*100 as percentage_of_people_vaccinated
from #PercentageVaccinated



--view(s) for visualizations 

create view 
PercentageVaccinated as 
select d.continent, d.location, d.date, d.population, v.new_vaccinations,
SUM(cast(v.new_vaccinations as float)) OVER (partition by d.location
order by d.location, d.date) as total_people_vaccinated
from CovidDeaths d
join CovidVaccinations v
on d.location = v.location
and d.date = v.date
where d.continent is not null






