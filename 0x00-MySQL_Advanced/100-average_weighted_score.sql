-- Calculate weighted average

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;

    -- Calculate total scire and total weight for the user
    SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate and update the average weighted score
    IF total_weight > 0 THEN
        UPDATE users
	SET average_score = total_weighted_score / total_weight
	WHERE id = user_id;
    END IF;
END //

DELIMITER ;
