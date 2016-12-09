-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema FPL
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema FPL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `FPL` DEFAULT CHARACTER SET latin1 ;
USE `FPL` ;

-- -----------------------------------------------------
-- Table `FPL`.`Team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`Team` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `rank` INT NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `region` VARCHAR(45) NOT NULL,
  `stadium` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`Player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`Player` (
  `pid` INT NOT NULL,
  `name` VARCHAR(150) NOT NULL,
  `nationality` VARCHAR(45) NOT NULL,
  `position` VARCHAR(3) NOT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE INDEX `pid_UNIQUE` (`pid` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`CurrentSeasonStats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`CurrentSeasonStats` (
  `total_points` INT NOT NULL,
  `mins_played` INT NOT NULL,
  `goals_scored` INT NOT NULL,
  `assists` INT NOT NULL,
  `clean_sheets` INT NOT NULL,
  `goals_conceded` INT NOT NULL,
  `own_goals` INT NOT NULL,
  `penalties_saved` INT NOT NULL,
  `penalties_missed` INT NOT NULL,
  `yellow_cards` INT NOT NULL,
  `red_cards` INT NOT NULL,
  `saves` INT NOT NULL,
  `ea_index` INT NOT NULL,
  `influence` DOUBLE NOT NULL,
  `creativity` DOUBLE NOT NULL,
  `threat` DOUBLE NOT NULL,
  `ict_index` DOUBLE NOT NULL,
  `Player_pid` INT NOT NULL,
  INDEX `fk_CurrentSeasonStats_Player1_idx` (`Player_pid` ASC),
  CONSTRAINT `fk_CurrentSeasonStats_Player1`
    FOREIGN KEY (`Player_pid`)
    REFERENCES `FPL`.`Player` (`pid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`History`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`History` (
  `league_trophies` INT NOT NULL,
  `fa_trophies` INT NOT NULL,
  `efl_trophies` INT NOT NULL,
  `wins` INT NOT NULL,
  `losses` INT NOT NULL,
  `draws` INT NOT NULL,
  `Team_id` INT NOT NULL,
  INDEX `fk_History_Team1_idx` (`Team_id` ASC),
  CONSTRAINT `fk_History_Team1`
    FOREIGN KEY (`Team_id`)
    REFERENCES `FPL`.`Team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`Manager`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`Manager` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `birth_country` VARCHAR(45) NOT NULL,
  `years_as_manager` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`Result`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`Result` (
  `id` INT NOT NULL,
  `gameweek` INT NOT NULL,
  `home_score` INT NULL,
  `away_score` INT NULL,
  `home_Team_id` INT NOT NULL,
  `away_Team_id` INT NOT NULL,
  `home_Manager_id` INT NOT NULL,
  `away_Manager_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `mid_UNIQUE` (`id` ASC),
  INDEX `fk_Result_Team1_idx` (`home_Team_id` ASC),
  INDEX `fk_Result_Team2_idx` (`away_Team_id` ASC),
  INDEX `fk_Result_Manager1_idx` (`home_Manager_id` ASC),
  INDEX `fk_Result_Manager2_idx` (`away_Manager_id` ASC),
  CONSTRAINT `fk_Result_Team1`
    FOREIGN KEY (`home_Team_id`)
    REFERENCES `FPL`.`Team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Result_Team2`
    FOREIGN KEY (`away_Team_id`)
    REFERENCES `FPL`.`Team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Result_Manager1`
    FOREIGN KEY (`home_Manager_id`)
    REFERENCES `FPL`.`Manager` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Result_Manager2`
    FOREIGN KEY (`away_Manager_id`)
    REFERENCES `FPL`.`Manager` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`TotalPastStats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`TotalPastStats` (
  `total_points` INT NOT NULL,
  `mins_played` INT NOT NULL,
  `goals_scored` INT NOT NULL,
  `assists` INT NOT NULL,
  `clean_sheets` INT NOT NULL,
  `goals_conceded` INT NOT NULL,
  `own_goals` INT NOT NULL,
  `penalties_saved` INT NOT NULL,
  `penalties_missed` INT NOT NULL,
  `yellow_cards` INT NOT NULL,
  `red_cards` INT NOT NULL,
  `saves` INT NOT NULL,
  `ea_index` INT NOT NULL,
  `previous_pl_seasons` INT NOT NULL,
  `Player_pid` INT NOT NULL,
  INDEX `fk_PastOverallStats_Players1_idx` (`Player_pid` ASC),
  CONSTRAINT `fk_PastOverallStats_Players1`
    FOREIGN KEY (`Player_pid`)
    REFERENCES `FPL`.`Player` (`pid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `FPL`.`PlayerResultStats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FPL`.`PlayerResultStats` (
  `pmid` INT NOT NULL,
  `points` INT NOT NULL,
  `mins_played` INT NOT NULL,
  `goals_scored` INT NOT NULL,
  `assits` INT NOT NULL,
  `clean_sheet` TINYINT(1) NOT NULL,
  `goals_conceded` INT NOT NULL,
  `own_goals` INT NOT NULL,
  `penalties_saved` INT NOT NULL,
  `penalties_missed` INT NOT NULL,
  `yellow_cards` INT NOT NULL,
  `red_cards` INT NOT NULL,
  `saves` INT NOT NULL,
  `influence` DOUBLE NOT NULL,
  `creativity` DOUBLE NOT NULL,
  `threat` DOUBLE NOT NULL,
  `ict_index` DOUBLE NOT NULL,
  `Result_id` INT NOT NULL,
  `Player_pid` INT NOT NULL,
  INDEX `fk_Player_has_Match_Match1_idx` (`Result_id` ASC),
  INDEX `fk_Player_has_Match_Player1_idx` (`Player_pid` ASC),
  UNIQUE INDEX `pmid_UNIQUE` (`pmid` ASC),
  PRIMARY KEY (`pmid`),
  CONSTRAINT `fk_Player_has_Match_Match1`
    FOREIGN KEY (`Result_id`)
    REFERENCES `FPL`.`Result` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Player_has_Match_Player1`
    FOREIGN KEY (`Player_pid`)
    REFERENCES `FPL`.`Player` (`pid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
