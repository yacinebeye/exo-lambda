resource "aws_iam_role" "lambda_role" {
  name = "iam_execrole_lambda"
  assume_role_policy = data "aws_iam_policy_document" "assume_role_policy.json
}
 

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
  
   principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}