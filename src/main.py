from estimator import estimate_density

def main():
    print("🚀 Starting Crowd_Density_Estimation")
    sample_file = r"data/raw/sample_crowd.jpg"  # put a test crowd image here
    result = estimate_density(sample_file)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
