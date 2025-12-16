-- Замена материала "дерево" на "стекло" у всех коробок
UPDATE "Box"
SET
    "material" = 'стекло'
WHERE
	"material" LIKE 'дерево'
;

-- Увеличение ширины на 7 у тех коробок, у которых
-- произведение длины на высоту больше 10
UPDATE "Box"
SET
	"width" = "width" + 7
WHERE
	"length" * "height" > 10
;

-- Удаление коробок объёмом меньше 6 куб. ед.
DELETE FROM "Box"
WHERE "width" * "length" * "height" < 6;
