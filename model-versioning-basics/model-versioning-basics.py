def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    models = sorted(models, key=lambda m: m["timestamp"], reverse=True)
    models = sorted(models, key=lambda m: m["latency"], reverse=False)
    models = sorted(models, key=lambda m: m["accuracy"], reverse=True)

    return models[0]["name"]
    pass