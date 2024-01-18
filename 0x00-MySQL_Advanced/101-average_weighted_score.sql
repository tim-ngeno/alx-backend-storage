-- Create a stored procedure to calculate average weighted score

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE current_user_id INT;

    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO current_user_id;
	IF done THEN
	    LEAVE user_loop;
	END IF;
  -- Separate block for local variables
        BEGIN
            DECLARE total_weighted_score FLOAT;
            DECLARE total_weight FLOAT;

            -- Calculate total weighted score and total weight for the user
            SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_weighted_score, total_weight
            FROM corrections c
            JOIN projects p ON c.project_id = p.id
            WHERE c.user_id = current_user_id;

            -- Calculate and update the average weighted score for the user
            IF total_weight > 0 THEN
                UPDATE users
                SET average_score = total_weighted_score / total_weight
                WHERE id = current_user_id;
            END IF;
        END; -- End of the separate block

    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;
