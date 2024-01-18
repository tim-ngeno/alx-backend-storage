-- Create a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student


-- Create the average_scores table if it doesn't exist
CREATE TABLE IF NOT EXISTS average_scores (
    user_id INT,
    average_score DECIMAL(10, 2),
    PRIMARY KEY (user_id)
);

-- Create the stored procedure script
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_count INT;
    DECLARE avg_score DECIMAL(10, 2);

    -- Compute the total score and count of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score
    IF total_count > 0 THEN
        SET avg_score = total_score / total_count;
    ELSE
        SET avg_score = 0; -- Avoid division by zero
    END IF;

    -- Store the average score in the average_scores table
    INSERT INTO average_scores (user_id, average_score)
    VALUES (user_id, avg_score);

END;
//
DELIMITER ;
