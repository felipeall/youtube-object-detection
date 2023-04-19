variable "infra_credentials" {
  description = "The file with GCP Service Account infra credentials"
  type        = string
  default     = "infra_service_account.json"
}

variable "project_id" {
  description = "The name of the project"
  type        = string
  default     = "gcloud-yod"
}

variable "region" {
  description = "The default compute region"
  type        = string
  default     = "southamerica-east1"
}

variable "zone" {
  description = "The default compute zone"
  type        = string
  default     = "southamerica-east1-a"
}

variable "repository" {
  description = "The name of the Artifact Registry repository to be created"
  type        = string
  default     = "docker-repository"
}

variable "docker_image" {
  description = "The name of the Docker image in the Artifact Registry repository to be deployed to Cloud Run"
  type        = string
  default     = "youtube-object-detection-api"
}

variable "first_time" {
  description = "Boolean flag to indicate if this is the first time the application is running"
  type        = bool
  default     = true
}
