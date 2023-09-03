import resource

# Get the current memory limit
soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_AS)

# Convert the limits to human-readable format (optional)
soft_limit_MB = soft_limit / (1024 * 1024)  # Convert to megabytes
hard_limit_MB = hard_limit / (1024 * 1024)

print(soft_limit)

print(f"Soft memory limit: {soft_limit_MB} MB")
print(f"Hard memory limit: {hard_limit_MB} MB")
