for i in range(2,20):
        with open(f"table/Multipaction{i}","w")as f:    
            for j in range(1,11):
                f.write(f"{i}x{j}={i*j}")
        break
